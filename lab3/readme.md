# Lab 3: C Bindings for Python

When we write Systems Code, we often build libraries that other programs can use. 
In Lab-2 we built core data structures for an assembler: a Symbol Table and an Opcode Table.
In this lab, we will access these libraries from Python using C bindings.
For that ensure you have `ctypesgen` installed: `pip install ctypesgen`.[^python-venv]

## Sample lab3.py and lab3.c
Refer to the provided `lab3.py` and `lab3.c` files for sample implementations that test the Symbol Table and Opcode Table from Lab-2.

## Python and C are Friends
To make Python talk to C, we need to bridge the gap between Python's high-level objects and C's low-level memory management.

### Shared Objects (`.so`)
An `.so` file contains compiled C code that isn't a standalone program (it has no main function).
Instead, it is loaded into memory at runtime by other programs (like the Python interpreter).
To create a shared object from your C code, you compile it with special flags:

* -shared: Tells GCC to produce a shared library, not an executable.
* -fPIC: "Position Independent Code." This ensures the code can be loaded anywhere in memory, which is required for shared libraries.

```Bash
# The shared library combines symtab.c and optab.c and will be named liblab3.so 
gcc -shared -fPIC -o liblab3.so symtab.c optab.c
```

### Bindings
Bindings are the "glue code" that acts as a translator to tell Python how a C struct looks like or how to call a C function.
While you can manually write these bindings using the `ctypes` library, it is tedious and error-prone.
`ctypesgen` is a tool that automates this.
It reads your C header files (`.h`), analyzes the structs and function signatures, and auto-generates a pure Python file that can be imported as if it were a normal Python module.

```Bash
# Note the missing prefix `lib`: -l lab3 tells it to link against liblab3.so in the current directory (-L .) 
ctypesgen -l lab3 -L . symtab.h optab.h -o bindings.py
```

### Running the Tests
When you run the Python script, the OS needs to know where to find your custom `.so` file.

```Bash
python3 lab3.py  #  will fail
DYLD_LIBRARY_PATH=. LD_LIBRARY_PATH=. python3 lab3.py # correct way
```

## Write the Makefile to build and test your libraries
Write your own Makefile that automates the build and test of your libraries.
If you are stuck for a long time, first look at the provided Makefile for Lab-2 and if you are still stuck, look at the provided Makefile for Lab-3.

To test your implementation, run `make test`.

## Literal Table
Until now in this lab, we built the shared library `liblab3.so` that can be used in Python via the generated `bindings.py` file.
While we can complete the data structure suite by implementing a Literal Table in `littab.c` that handles constants like `=C'EOF'` or `=X'05'`, for convenience we will implement it in Python directly in `littab.py`.
If at the end of the course you (still) feel comfortable with FFIs and C, you can always come back and implement it in C later.
Use the following interface for the Literal Table:

```Python
class LitTab:
    def __init__(self):
        # Initialize your literal table data structure here
        pass
        
    def add_literal(self, literal: str) -> None:
        # Called during Pass 1: Adds a literal (e.g., =C'EOF') without an address.
        # Logic: Parse the literal, calculate length, store it.
        pass
        
    def assign_addresses(self, current_locctr: int) -> int:
        # Called when Assembler hits LTORG or END.
        # Logic: Assigns addresses to unassigned literals.
        # Returns: The new implementation of LOCCTR after allocation.
        pass
        
    def get_address(self, literal: str) -> int:
        # Called during Pass 2: Returns the assigned address.
        pass
```



## Steps to Complete the Lab
- Implement `littab.py` following the provided interface.
- Update `lab3.py` to test the Literal Table functions.
- Get ready for Lab-4 where we will integrate all these tables into an assembler!

[^python-venv]: It is recommended to use a Python virtual environment to manage dependencies. You can create one using `python3 -m venv venv` and activate it with `source venv/bin/activate`. This will help keep your project dependencies isolated.
