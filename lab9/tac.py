from dataclasses import dataclass
from ast_nodes import ASTNode, Char_Literal, Id, Number, Program, ReturnStmt, String_Literal, VarDecl, ArrayDecl, ArrayAccess, FuncDecl, ReadStmt, WhileStmt, WriteStmt, GotoStmt, LabelStmt, Block, IfStmt, FuncCall, Assign

@dataclass
class TACInstruction:
    op: str
    arg1: str
    arg2: str
    result: str

    def __str__(self):  
        arg1 = self.arg1 if self.arg1 is not None else ''
        arg2 = self.arg2 if self.arg2 is not None else ''
        result = self.result if self.result is not None else ''
        if self.op == 'U-':
            return f"{result} = -{arg1}".strip()
        elif self.op == '=':
            return f"{result} = {arg1}".strip()
        elif self.op in ['goto', 'label', 'param', 'call', 'return']:
            # Format control flow/function instructions
            return f"{self.op} {arg1} {arg2} {result}".strip()
        elif self.op == 'goto_label_id':
            return f"goto_label L[{arg1}]".strip()
        elif self.op == 'if_false':
            return f"ifFalse {arg1} goto {result}".strip()
        elif self.op in ['read', 'write']:
            # For read, the target is in 'result'. For write, the value is in 'arg1'.
            target = self.result if self.op == 'read' else self.arg1
            return f"{self.op} {target}".strip()
        elif self.op in ['declare_int', 'declare_int_array', 'declare_char', 'declare_char_array']:
            return f"{self.op} {result} {arg1} {arg2}".strip()
        elif self.op in ['[]=']:
            return f"{result}[{arg1}] = {arg2}".strip()
        elif self.op in ['[]']:
            return f"{result} = {arg1}[{arg2}]".strip()
        else:
            return f"{result} = {arg1} {self.op} {arg2}".strip()


class TACProgram:
    STACK_SIZE = 1000  # for recursive calls
    STACK_NAME = "__s__"  # for recursive calls
    STACK_POINTER_NAME = "__sp__"  # for recursive calls
    def __init__(self):
        self.instructions: list[TACInstruction] = []
        self.temp_count: int = 0
        self.label_count: int = 0
        
        # Add tracking for caller-save mechanics
        self.current_func_name = ""
        self.current_func_vars = []
        self.current_func_ret_addr = None
        
        self.__init_instructions()
    
    def __init_instructions(self):
        # declare stack for recursive calls
        self.emit('declare_int_array', self.STACK_SIZE, None, self.STACK_NAME)
        self.emit('declare_int', 1, None, self.STACK_POINTER_NAME)
        self.emit('=', '0', None, self.STACK_POINTER_NAME)
        # declare global return value register
        self.emit('declare_int', 1, None, '__ret_val__')
    
    def _get_local_vars(self, node: ASTNode) -> list[str]:
        locals_list = []
        if isinstance(node, Block):
            for stmt in node.statements:
                if isinstance(stmt, VarDecl):
                    locals_list.append(stmt.var_name)
                elif isinstance(stmt, IfStmt):
                    locals_list.extend(self._get_local_vars(stmt.then_branch))
                    if stmt.else_branch:
                        locals_list.extend(self._get_local_vars(stmt.else_branch))
                elif isinstance(stmt, WhileStmt):
                    locals_list.extend(self._get_local_vars(stmt.body))
        return locals_list

    def new_temp(self, data_type: str) -> str:
        temp_name = f"t{self.temp_count}"
        self.emit(f'declare_{data_type}', 1, None, temp_name)
        self.temp_count += 1
        return temp_name

    def new_label(self) -> str:
        label_name = f"L{self.label_count}"
        self.label_count += 1
        return label_name
    
    def _array_assign(self, array_name: str, index: str, value: str):
        self.emit('[]=', index, value, array_name)

    def emit(self, op, arg1=None, arg2=None, result=None):
        instr = TACInstruction(op, arg1, arg2, result)
        self.instructions.append(instr)

    def __str__(self):
        return "\n".join(str(instr) for instr in self.instructions)
    
    def generate(self, node: ASTNode):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')
    
    # --- Node Visitors ---
    def visit_Program(self, node: Program):
        for decl in node.declarations:
            self.generate(decl)
    
    def visit_Block(self, node: Block):
        for stmt in node.statements:
            self.generate(stmt)

    # --- Leaves ---
    def visit_Number(self, node: Number) -> str:
        return str(node.value)
    
    def visit_str(self, node: str) -> str:
        return node
    
    def visit_Id(self, node: Id) -> str:
        return node.name
    
    def visit_Char_Literal(self, node: Char_Literal) -> str:
        return f"'{node.value}'"
    
    def visit_String_Literal(self, node: String_Literal) -> str:
        return f'"{node.value}"'
    
    
    # --- Declarations ---
    def visit_VarDecl(self, node: VarDecl):
        self.emit(f'declare_{node.var_type}', 1, None, node.var_name)
    def visit_FuncDecl(self, node: FuncDecl):
        self.emit('label', result=node.func_name)
        
        self.current_func_name = node.func_name
        # Collect parameters and local variables for this scope
        self.current_func_vars = [p.var_name for p in node.params]
        self.current_func_vars.extend(self._get_local_vars(node.body))
        self.current_func_ret_addr = self.new_temp('int')

        # define locations for arguments
        for param in node.params:
            self.generate(param)  # This will emit the declaration for the parameter

        # Main doesn't have a caller to pop arguments from
        if node.func_name != 'main':
            # Pop Return Address
            self.emit('-', self.STACK_POINTER_NAME, '1', self.STACK_POINTER_NAME)
            self.emit('[]', self.STACK_NAME, self.STACK_POINTER_NAME, self.current_func_ret_addr)

            # Pop Parameters into their variables (Caller pushed them left-to-right, so we pop right-to-left)
            for param in reversed(node.params):
                self.emit('-', self.STACK_POINTER_NAME, '1', self.STACK_POINTER_NAME)
                self.emit('[]', self.STACK_NAME, self.STACK_POINTER_NAME, param.var_name)

        # Generate code for function body
        self.generate(node.body)
        
        # Implicit return for void functions
        if node.func_name != 'main':
            self.emit('goto_label_id', self.current_func_ret_addr, None, None)
    def visit_ArrayDecl(self, node: ArrayDecl):
        self.emit(f'declare_{node.var_type}_array', node.size, None, node.var_name)
    
    # --- Expressions (Post-Order Traversal) ---
    def visit_BinOp(self, node):
        left = self.generate(node.left)
        right = self.generate(node.right)
        result = self.new_temp("int") # Assuming all binary operations result in an integer for simplicity
        self.emit(node.op, left, right, result)
        return result
    def visit_UnaryOp(self, node):
        operand = self.generate(node.operand)
        result = self.new_temp("int") # Assuming unary operations also result in an integer
        assert(node.op in ['-'])  # Only handling negation for now
        self.emit(f'U{node.op}', operand, None, result)
        return result

    
    def visit_Assign(self, node):
        value = self.generate(node.value)

        if isinstance(node.target, ArrayAccess):
            # Handle array access on the left-hand side
            index_temp = self.generate(node.target.index)
            self._array_assign(node.target.var_name, index_temp, value)
            return node.target.var_name  # Return the array name for consistency
        else:
            self.emit('=', value, None, node.target)
        return node.target
    
    def visit_ExprStmt(self, node):
        if node.expr:
            self.generate(node.expr)
        else:
            # No expression, just a semicolon
            pass
    
    # --- I/O ---
    def visit_ReadStmt(self, node: ReadStmt):
        self.emit('read', None, None, node.var_name)
    
    def visit_WriteStmt(self, node: WriteStmt):
        value = self.generate(node.expr)
        self.emit('write', value, None, None)
    

    # --- Control Flow ---
    def visit_IfStmt(self, node: IfStmt):
        cond_temp = self.generate(node.condition)
        label_false = self.new_label()
        label_end = self.new_label()

        self.emit('if_false', cond_temp, None, label_false)

        self.generate(node.then_branch)
        self.emit('goto', None, None, label_end)

        self.emit('label', None, None, label_false)
        if node.else_branch:
            self.generate(node.else_branch)
        
        self.emit('label', None, None, label_end)
    
    def visit_WhileStmt(self, node: WhileStmt):
        label_start = self.new_label()
        label_end = self.new_label()

        self.emit('label', None, None, label_start)
        
        cond_temp = self.generate(node.condition)
        self.emit('if_false', cond_temp, None, label_end)

        self.generate(node.body)
        self.emit('goto', None, None, label_start)

        self.emit('label', None, None, label_end)
    
    # --- Array Access ---
    def visit_ArrayAccess(self, node: ArrayAccess):
        index_temp = self.generate(node.index)
        result = self.new_temp("int")  # Assuming array access results in an integer for simplicity
        self.emit('[]', node.var_name, index_temp, result)
        return result

    # --- Function Calls ---
    def visit_FuncCall(self, node: FuncCall):
        next_instruction_label = self.new_label()
        next_instruction_label_index = int(next_instruction_label[1:]) 
        
        # 1. SAVE CONTEXT: Save caller's variables & return address so recursion doesn't overwrite them
        vars_to_save = self.current_func_vars + [self.current_func_ret_addr]
        for v in vars_to_save:
            if v is not None:
                self._array_assign(self.STACK_NAME, self.STACK_POINTER_NAME, v)
                self.emit('+', self.STACK_POINTER_NAME, '1', self.STACK_POINTER_NAME)

        # 2. PUSH ARGS
        for arg in node.args:
            arg_temp = self.generate(arg)
            self._array_assign(self.STACK_NAME, self.STACK_POINTER_NAME, str(arg_temp))
            self.emit('+', self.STACK_POINTER_NAME, '1', self.STACK_POINTER_NAME)
        
        # 3. PUSH RETURN ADDRESS
        self._array_assign(self.STACK_NAME, self.STACK_POINTER_NAME, str(next_instruction_label_index))
        self.emit('+', self.STACK_POINTER_NAME, '1', self.STACK_POINTER_NAME)
        
        # 4. JUMP
        self.emit('goto', None, None, node.func_name) 

        # 5. RESUME Execution
        self.emit('label', None, None, next_instruction_label)

        # 6. RESTORE CONTEXT: Pop in reverse order to get our local state back
        for v in reversed(vars_to_save):
            if v is not None:
                self.emit('-', self.STACK_POINTER_NAME, '1', self.STACK_POINTER_NAME)
                self.emit('[]', self.STACK_NAME, self.STACK_POINTER_NAME, v)
        
        # 7. READ RETURN VALUE
        return_value = self.new_temp("int")
        self.emit('=', '__ret_val__', None, return_value)

        return return_value

    def visit_ReturnStmt(self, node: ReturnStmt):
        value = 0
        if node.value:
            value = self.generate(node.value)
        
        # Assign to global return register
        self.emit('=', str(value), None, '__ret_val__')

        # Jump back to caller via the saved return address (if we aren't main)
        if getattr(self, 'current_func_name', '') != 'main':
            self.emit('goto_label_id', self.current_func_ret_addr, None, None)
        

def get_tac(source_path, tac_path):
    from parser import MiniCParser
    from lexer import MiniCLexer
    lexer = MiniCLexer()
    parser = MiniCParser()

    with open(source_path, 'r') as f:
        text = f.read()

    tokens = lexer.tokenize(text)
    ast = parser.parse(tokens)
    
    program = TACProgram()
    if ast:
        program.generate(ast)
        with open(tac_path, 'w') as f:
            f.write(str(program))
        print(f"TAC generation successful! TAC code written to: {tac_path}")


if __name__ == "__main__":
    import sys
    import pprint
    
    if len(sys.argv) < 2:
        print("Usage: python tac.py <source.c>")
        sys.exit(1)

    source_path = sys.argv[1]
    tac_path = source_path.rsplit('.', 1)[0] + ".tac"
    get_tac(source_path, tac_path)