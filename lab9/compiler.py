import sys
from assembler import assemble_file
from sic import get_sic_assembly
from tac import get_tac


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compiler.py <source.c>")
        sys.exit(1)
    
    source_path = sys.argv[1]

    tac_path = source_path.rsplit('.', 1)[0] + ".tac"
    get_tac(source_path, tac_path)

    sic_path = source_path.rsplit('.', 1)[0] + ".sic"
    get_sic_assembly(source_path, sic_path)

    obj_path = source_path.rsplit('.', 1)[0] + ".obj"
    assemble_file(sic_path, obj_path)