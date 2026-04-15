# Lab 9: Three-Address Code Generation to SIC Assembly
In Labs 6 and 7, we implemented a Lexer and Parser for MiniC.
In Lab 8, we constructed the Abstract Syntax Tree (AST) produced by the Parser and generate the corresponding Three-Address Code (TAC).
In this lab, we will extend our TAC generation to produce SIC assembly code.


## The SIC Structure
Recall the SIC assembly language that we have been working with in Labs 1 to 5.
The main challenge in this lab is to translate the TAC instructions into equivalent SIC assembly instructions.
We will need to manage the use of registers and memory locations to ensure that the generated assembly code correctly implements the semantics of the original MiniC program.
We will also need to handle function calls, control flow, and I/O operations in the context of SIC assembly.
For that, we will use the explicit stack that we created in Lab 8.
Finally, since there is only a single `Accumulator` register in SIC, we will need to carefully manage the use of this register when translating TAC instructions that involve multiple operands.


### `sic.py`
The `sic.py` file contains the `SICGenerator` class, which provides methods for generating SIC assembly instructions and managing temporary variables and labels.
You will need to implement the missing cases (arithmetic and relational operators) in the `SICGenerator._translate_instruction()` method.
See, the implemented cases for reference.

You can provide a sample MiniC program to generate the SIC assembly: `python sic.py <source.c>`.

## Test
See the MiniC codes in `samples/` for testing your implementation.

- `python tac.py samples/add.c` will generate the Three-Address Code
- `python sic.py samples/add.c` will generate the SIC assembly code at `samples/add.sic`.
- `python assembler.py samples/add.sic` will generate the object file at `samples/add.sic.obj`.
- Alternatively, `python compiler.py samples/add.c` will generate the object file directly at `samples/add.obj`.
- `python ../simsic/simsic.py samples/add.obj` will run the object file using the SIC Simulator. Then, you can verify the output.

Since the generated code is SIC assembly, we can use the Assembler that we developed in Labs 1-5 to produce the object file.
Finally, we can run the object file using the SIC Simulator to verify that the generated assembly code correctly implements the semantics of the original MiniC program.

## tl;dr
- Implement the missing pieces of `SICGenerator` class in `sic.py`.
- Test your implementation by providing a sample MiniC program and generating the corresponding SIC assembly code.