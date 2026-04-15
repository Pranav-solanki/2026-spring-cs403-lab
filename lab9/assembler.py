from Assembler import Assembler, AssemblerError
import sys

def assemble_file(source_path, output_path):
    assembler = Assembler(source_path, output_path)
    try:
        assembler.assemble()
        print(f"Assembly successful! Object file generated at: {output_path}")
    except AssemblerError as e:
        print(f"Assembly failed with error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python assembler.py <source.asm> [output.obj]")
        sys.exit(1)
    
    source_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else source_path + ".obj"
    
    assemble_file(source_path, output_path)