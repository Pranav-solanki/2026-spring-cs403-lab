import sys
from tac import TACProgram, TACInstruction
STACK_POINTER_NAME = "__sp__"

class SICGenerator:
    def __init__(self):
        self.code = []
        self.data = []
        
        # Track different types of constants
        self.constants = set()        # For integers
        self.str_constants = {}       # For strings (maps '"text"' to 'STR_x')
        self.char_constants = {}      # For chars (maps "'c'" to 'CHR_x')
        
        self.pending_labels = []
        self.cond_counter = 0

    def emit_code(self, opcode: str, operand: str = ""):
        while len(self.pending_labels) > 1:
            self.code.append(f"{self.pending_labels.pop(0):<10}\n")
        # Format cleanly in typical assembly columns
        label = self.pending_labels.pop(0) if self.pending_labels else ""
        self.code.append(f"{label:<10} {opcode:<8} {operand}")

    def emit_data(self, label: str, directive: str, operand: str):
        self.data.append(f"{label:<10} {directive:<8} {operand}")

    def is_number(self, val: str) -> bool:
        try:
            int(val)
            return True
        except (ValueError, TypeError):
            return False

    def get_operand(self, val: str) -> str:
        """
        Vanilla SIC has no immediate addressing (#). 
        This automatically registers numbers, strings, and chars as 
        constants and returns their memory label.
        """
        if val is None:
            return ""

        # Handle Integers
        if self.is_number(val):
            num = int(val)
            self.constants.add(num)
            if num < 0:
                return f"C_N{abs(num)}"
            return f"C_{num}"
            
        # Handle String Literals (e.g. "Enter n")
        elif val.startswith('"') and val.endswith('"'):
            if val not in self.str_constants:
                self.str_constants[val] = f"STR_{len(self.str_constants)}"
            return self.str_constants[val]
            
        # Handle Character Literals (e.g. 'A')
        elif val.startswith("'") and val.endswith("'"):
            if val not in self.char_constants:
                self.char_constants[val] = f"CHR_{len(self.char_constants)}"
            return self.char_constants[val]
            
        return val

    def generate(self, tac_program: TACProgram) -> str:
        # Pre-seed essential constants
        self.constants.update([0, 1, 3])
        self.emit_data("X_TEMP", "RESW", "1")
        self.emit_data("DISP_VAR", "RESW", "1")
        
        # Standard device placeholders for Read/Write
        self.emit_data("INDEV", "BYTE", "X'F1'")
        self.emit_data("OUTDEV", "BYTE", "X'05'")

        self.emit_code("START", "0")
        self.emit_code("J", "main") #MIGHT need to delete this
        
        # Collect all return labels for the Dispatcher
        return_labels = []

        for instr in tac_program.instructions:
            print(f"DEBUG: Processing TAC instruction: {instr}")  # Debug statement
            if instr.op == 'label' and instr.result and instr.result.startswith('L'):
                return_labels.append(instr.result)
            self._translate_instruction(instr)

        # --- EOP unless going to dispatch ---
        self.pending_labels.append("EOP")
        self.emit_code("J", "EOP")

        # --- CENTRAL DISPATCHER ---
        self.pending_labels.append("DISPATCH")
        self.emit_code("LDA", "DISP_VAR")
        for lbl in return_labels:
            lbl_id = int(lbl[1:])  # e.g., 'L5' -> 5
            self.constants.add(lbl_id)
            const_name = self.get_operand(str(lbl_id))
            self.emit_code("COMP", const_name)
            self.emit_code("JEQ", lbl)
        
        # Infinite loop fallback if dispatch fails
        self.pending_labels.append("EOPSAFE")
        self.emit_code("J", "EOPSAFE")
        # Mark End of Code Execution 
        # (Must happen before we join the assembly strings)
        self.emit_code("END", "START")

        # --- DATA SECTION GENERATOR ---
        
        # 1. Generate numeric constants
        for c in sorted(self.constants):
            lbl = f"C_N{abs(c)}" if c < 0 else f"C_{c}"
            self.emit_data(lbl, "WORD", str(c))

        # 2. Generate string constants
        for val, lbl in self.str_constants.items():
            # Strip double quotes and use SIC BYTE C'...' format
            inner_str = val[1:-1]
            self.emit_data(lbl, "BYTE", f"C'{inner_str}'")
            
        # 3. Generate char constants
        for val, lbl in self.char_constants.items():
            # Strip single quotes and use SIC BYTE C'...' format
            inner_char = val[1:-1]
            self.emit_data(lbl, "BYTE", f"C'{inner_char}'")

        # Assemble final strings
        assembly = ".\t --- CODE SECTION ---\n"
        assembly += "\n".join(self.code[:-1])  # Exclude END directive for now
        assembly += "\n\n.\t --- DATA SECTION ---\n"
        assembly += "\n".join(self.data)
        assembly += f"\n{self.code[-1]}"  # Append END directive at the end of the assembly
        
        return assembly

    def _translate_instruction(self, instr: TACInstruction):
        op = instr.op
        
        # --- Declarations ---
        if op == 'declare_int':
            self.emit_data(instr.result, "RESW", "1")
        elif op == 'declare_char':
            self.emit_data(instr.result, "RESB", "1")
        elif op == 'declare_int_array':
            self.emit_data(instr.result, "RESW", instr.arg1)
        elif op == 'declare_char_array':
            self.emit_data(instr.result, "RESB", instr.arg1)
            
        # --- Labels ---
        elif op == 'label':
            self.pending_labels.append(instr.result)
            
        # --- Assignments ---
        elif op == '=':
            self.emit_code("LDA", self.get_operand(instr.arg1))
            self.emit_code("STA", instr.result)
            
        # --- Arithmetic ---
        elif op in ['+', '-', '*', '/']:
            pass
            #implement this
            
        # --- Relational Operators ---
        elif op in ['==', '!=', '<', '<=', '>', '>=']:
            pass
            #implement this

        # --- Control Flow ---
        elif op == 'goto':
            print(f"DEBUG: Translating goto to {instr.result} of {instr}")  # Debug statement
            self.emit_code("J", instr.result)
            
        elif op == 'if_false':
            self.emit_code("LDA", self.get_operand(instr.arg1))
            self.emit_code("COMP", self.get_operand("0"))
            self.emit_code("JEQ", instr.result)
            
        elif op == 'goto_label_id':
            self.emit_code("LDA", self.get_operand(instr.arg1))
            self.emit_code("STA", "DISP_VAR")
            self.emit_code("J", "DISPATCH")
            
        # --- Array Operations ---
        elif op == '[]=':
            self.emit_code("LDA", self.get_operand(instr.arg1)) 
            self.emit_code("MUL", self.get_operand("3"))        
            self.emit_code("STA", "X_TEMP")
            self.emit_code("LDX", "X_TEMP")                     
            self.emit_code("LDA", self.get_operand(instr.arg2)) 
            self.emit_code("STA", f"{instr.result},X")          
            
        elif op == '[]':
            self.emit_code("LDA", self.get_operand(instr.arg2)) 
            self.emit_code("MUL", self.get_operand("3"))        
            self.emit_code("STA", "X_TEMP")
            self.emit_code("LDX", "X_TEMP")                     
            self.emit_code("LDA", f"{instr.arg1},X")            
            self.emit_code("STA", instr.result)                 
            
        # --- I/O Operations ---
        elif op == 'read':
            self.emit_code("RD", "INDEV")
            self.emit_code("STA", instr.result)
            
        elif op == 'write':
            # writes CHAR. should convert into to char here
            self.emit_code("LDA", self.get_operand(instr.arg1))
            self.emit_code("WD", "OUTDEV")


def get_sic_assembly(source_path: str, output_path: str) -> None:
    from lexer import MiniCLexer
    from parser import MiniCParser
    lexer = MiniCLexer()
    parser = MiniCParser()
    
    with open(source_path, 'r') as f:
        text = f.read()
    tokens = lexer.tokenize(text)
    ast = parser.parse(tokens)
    
    tac_program = TACProgram()
    
    if ast:
        # Generate Three-Address Code first
        tac_program.generate(ast)
        
        # Translate TAC to Vanilla SIC
        sic_generator = SICGenerator()
        sic_assembly = sic_generator.generate(tac_program)
        with open(output_path, 'w') as f:
            f.write(sic_assembly)
            print(f"SIC assembly generated at: {output_path}")

if __name__ == "__main__":
    from lexer import MiniCLexer
    from parser import MiniCParser

    if len(sys.argv) < 2:
        print("Usage: python sic.py <source.c>")
        sys.exit(1)

    source_path = sys.argv[1]
    output_path = source_path.rsplit('.', 1)[0] + ".sic"
    get_sic_assembly(source_path, output_path)

