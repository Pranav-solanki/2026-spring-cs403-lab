import sys
from sly import Parser
import pprint
from lexer import MiniCLexer
from ast_nodes import Program, VarDecl, ArrayDecl, FuncDecl, Block, IfStmt, WhileStmt, ReturnStmt, BinOp, Assign, Number, ExprStmt, Id, ArrayAccess, ReadStmt, WriteStmt, FuncCall, GotoStmt, LabelStmt

class MiniCParser(Parser):
    tokens = MiniCLexer.tokens

    # Precedence correctly resolves ambiguity for math and the "Dangling Else"
    precedence = (
        ('nonassoc', LOWER_THAN_ELSE),
        ('nonassoc', ELSE),
        ('right', ASSIGN),
        ('left', OR),
        ('left', AND),
        ('left', EQ, NE),
        ('left', LT, LE, GT, GE),
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE, MOD),
        ('right', NOT, AT, UMINUS), # UMINUS is for unary minus
    )

    # --- Program and Declarations ---
    @_('program_elements')
    def program(self, p):
        # states that a valid program consists entirely of program_elements.
        return Program(p.program_elements)
    
    @_('program_elements decl',
       'program_elements include_stmt')
    def program_elements(self, p):
        # RECURSIVE CASE: to build a list, you use left recursion.
        if p[1] is not None:
            p.program_elements.append(p[1])
        return p.program_elements

    @_('decl', 'include_stmt')
    def program_elements(self, p):
        # BASE CASE: SLY doesn't have a built-in "match zero or more" (*) regex operator
        return [p[0]] if p[0] is not None else []

    @_('INCLUDE')
    def include_stmt(self, p):
        pass # Ignore for now. In future, "copy" the included file's AST into the current one.

    @_('var_decl', 'array_decl', 'func_decl')
    def decl(self, p):
        return p[0]

    @_('INT', 'VOID', 'CHAR')
    def type_spec(self, p):
        return p[0]

    @_('type_spec ID SEMI')
    def var_decl(self, p):
        return VarDecl(p.type_spec, p.ID)

    @_('type_spec ID LBRACKET NUMBER RBRACKET SEMI')
    def array_decl(self, p):
        # complete this
        pass

    # --- Functions and Parameters ---
    @_('type_spec ID LPAREN param_list RPAREN compound_stmt',
       'type_spec ID LPAREN VOID RPAREN compound_stmt',
       'type_spec ID LPAREN RPAREN compound_stmt')
    def func_decl(self, p):
        # complete this
        pass

    @_('param_list COMMA param')
    def param_list(self, p):
        # complete this
        pass

    @_('param')
    def param_list(self, p):
        # complete this
        pass

    @_('type_spec ID')
    def param(self, p):
        return VarDecl(p.type_spec, p.ID)
        
    @_('type_spec ID LBRACKET RBRACKET')
    def param(self, p):
        # complete this
        pass

    # --- Statements and Blocks ---
    @_('LBRACE block_item_list RBRACE')
    def compound_stmt(self, p):
        return Block(p.block_item_list)

    @_('LBRACE RBRACE')
    def compound_stmt(self, p):
        return Block([])

    @_('block_item_list block_item')
    def block_item_list(self, p):
        p.block_item_list.append(p.block_item)
        return p.block_item_list

    @_('block_item')
    def block_item_list(self, p):
        return [p.block_item]

    # Allows interleaving of declarations and statements (C99 style)
    @_('var_decl', 'statement')
    def block_item(self, p):
        return p[0]

    @_('expression_stmt', 'compound_stmt', 'selection_stmt', 
       'iteration_stmt', 'return_stmt', 'io_stmt', 'jump_stmt', 'label_stmt')
    def statement(self, p):
        return p[0]

    @_('expr SEMI')
    def expression_stmt(self, p):
        return ExprStmt(p.expr)

    @_('SEMI')
    def expression_stmt(self, p):
        return ExprStmt(None)

    @_('IF LPAREN expr RPAREN statement %prec LOWER_THAN_ELSE')
    def selection_stmt(self, p):
        return IfStmt(p.expr, p.statement, None)

    @_('IF LPAREN expr RPAREN statement ELSE statement')
    def selection_stmt(self, p):
        return IfStmt(p.expr, p.statement0, p.statement1)

    @_('WHILE LPAREN expr RPAREN statement')
    def iteration_stmt(self, p):
        # complete this
        pass

    @_('RETURN SEMI')
    def return_stmt(self, p):
        return ReturnStmt(None)

    @_('RETURN expr SEMI')
    def return_stmt(self, p):
        # complete this
        pass

    @_('READ LPAREN ID RPAREN SEMI')
    def io_stmt(self, p):
        return ReadStmt(p.ID)

    @_('WRITE LPAREN expr RPAREN SEMI')
    def io_stmt(self, p):
        return WriteStmt(p.expr)

    @_('GOTO expr SEMI')
    def jump_stmt(self, p):
        return GotoStmt(p.expr)

    @_('ID COLON')
    def label_stmt(self, p):
        return LabelStmt(p.ID)

    # --- Expressions ---
    @_('ID ASSIGN expr',
       'ID LBRACKET expr RBRACKET ASSIGN expr')
    def expr(self, p):
        if hasattr(p, 'LBRACKET'):
            target = ArrayAccess(p.ID, p.expr0)
            val = p.expr1
        else:
            target =p.ID
            val = p.expr
        return Assign(target, val)

    @_('expr PLUS expr', 'expr MINUS expr', 'expr TIMES expr',
    'expr DIVIDE expr', 'expr MOD expr', 'expr EQ expr',
       'expr NE expr', 'expr LT expr', 'expr LE expr',
       'expr GT expr', 'expr GE expr', 'expr AND expr', 'expr OR expr')
    def expr(self, p):
        return BinOp(p[1], p.expr0, p.expr1)
        
    @_('NOT expr', 'AT expr')
    def expr(self, p):
        # complete this
        pass

    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        # complete this
        pass

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('ID')
    def expr(self, p):
        return Id(p.ID)

    @_('ID LBRACKET expr RBRACKET')
    def expr(self, p):
        return ArrayAccess(p.ID, p.expr)

    @_('NUMBER')
    def expr(self, p):
        return Number(int(p.NUMBER))
        
    @_('CHAR_LITERAL')
    def expr(self, p):
        return str(p.CHAR_LITERAL)
        
    @_('STRING_LITERAL')
    def expr(self, p):
        return str(p.STRING_LITERAL)

    @_('ID LPAREN arg_list RPAREN',
       'ID LPAREN RPAREN')
    def expr(self, p):
        args = p.arg_list if hasattr(p, 'arg_list') else []
        return FuncCall(p.ID, args)

    @_('arg_list COMMA expr')
    def arg_list(self, p):
        p.arg_list.append(p.expr)
        return p.arg_list

    @_('expr')
    def arg_list(self, p):
        return [p.expr]

    # --- Error Handling ---
    def error(self, p):
        if p:
            print(f"Syntax error at token {p.type} ('{p.value}') on line {p.lineno}")
        else:
            print("Syntax error at EOF")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python parser.py <source.c>")
        sys.exit(1)

    lexer = MiniCLexer()
    parser = MiniCParser()

    with open(sys.argv[1], 'r') as f:
        text = f.read()

    tokens = lexer.tokenize(text)
    ast = parser.parse(tokens)
    
    if ast:
        pprint.pprint(ast)