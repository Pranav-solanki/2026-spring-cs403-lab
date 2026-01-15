import sys
import ctypes
import bindings 

def main():
    print("--- LAB 3: AUTO-GENERATED BINDINGS ---")
    
    # Initialize
    bindings.init_symtab()

    print("\nTesting Symbol Table Insertion...")
    # Strings in C still need bytes, but ctypesgen handles the function calls
    bindings.insert_symbol(b"COPY", 0x1000)
    bindings.insert_symbol(b"FIRST", 0x1003)
    bindings.insert_symbol(b"CLOOP", 0x1006)

    # Duplicate Check
    if not bindings.insert_symbol(b"COPY", 0x2000):
        print("Duplicate 'COPY' rejected correctly.")

    # Search
    addr = bindings.search_symbol(b"CLOOP")
    if addr != -1:
        print(f"Found 'CLOOP' at Address: {addr:X}")
    
    sys.stdout.flush()
    bindings.display_symtab()
    libc = ctypes.CDLL(None)
    libc.fflush(None)

    print("\nTesting Opcode Table Lookup...")
    for mnemonic in ["LDA", "STA", "ADD", "XYZ"]:
        res = bindings.search_optab(mnemonic)
        if res:
            print(f"{mnemonic} -> {res}")
        else:
            print(f"{mnemonic} -> Invalid Opcode")

if __name__ == "__main__":
    main()