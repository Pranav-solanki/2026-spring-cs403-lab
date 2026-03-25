import sys
import os
from lexer import MiniCLexer

SAMPLES_DIR = "samples/"
TESTS = [f"{SAMPLES_DIR}{i}.c" for i in range(1, 1+5)] 
LEXER_ERRORS = [f"{SAMPLES_DIR}LexerError{i}.c" for i in range(1, 1+1)]

def token_path(c_path: str) -> str:
    return c_path + ".tokens"
def gold_path(c_path: str) -> str:
    return c_path + ".tokens.gold"

def compare_files(file1_path: str, file2_path: str) -> bool:
    try:
        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            content1 = f1.read().strip()
            content2 = f2.read().strip()
            return content1 == content2
    except FileNotFoundError:
        return False

def run_lexer(input_path: str, output_path: str):
    """
    Runs the MiniCLexer on input_path and writes formatted tokens to output_path.
    """
    lexer = MiniCLexer()
    
    with open(input_path, 'r') as f:
        data = f.read()

    tokens = lexer.tokenize(data)

    with open(output_path, 'w') as f:
        f.write(f"{'TOKEN TYPE':<20} {'VALUE':<20} {'LINE':<5}\n")
        f.write("-" * 50 + "\n")
        
        for tok in tokens:
            val = str(tok.value).replace('\n', '\\n')
            f.write(f"{tok.type:<20} {val:<20} {tok.lineno:<5}\n")

def _make_gold_standard():
    print("Generating gold standard files...")
    for c_path in TESTS + LEXER_ERRORS:
        run_lexer(c_path, gold_path(c_path))
        print(f"Generated {gold_path(c_path)}")

def main():
    # 1. Run Valid Tests
    print("\n--- Running Valid Tests ---")
    for c_path in TESTS:
        print(f"Testing Lexer on {c_path}...", end=" ")
        run_lexer(c_path, token_path(c_path))
            
        if compare_files(token_path(c_path), gold_path(c_path)):
            print("✅ PASSED")
        else:
            raise AssertionError("❌FAILED")
            exit(1) # Stop on first failure for debugging

    # 2. Run Error Tests
    print("\n--- Running Error Tests ---")
    for c_path in LEXER_ERRORS:    
        print(f"Testing Lexer Error handling on {c_path}...", end=" ")
        run_lexer(c_path, token_path(c_path))
        if compare_files(token_path(c_path), gold_path(c_path)):
            print("✅ PASSED (Produced expected partial token stream)")
        else:
            raise AssertionError("❌FAILED")
            exit(1) # Stop on first failure for debugging
    
    print("\n✅ All tests passed successfully!")

if __name__ == "__main__":
    # _make_gold_standard() # Uncomment this line to regenerate gold files
    main()