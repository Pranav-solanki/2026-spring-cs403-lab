# Lab 7: MiniC Parser
In Lab 6, we implemented a Lexer for MiniC.
In this lab, we will take the tokens produced by the Lexer and build a Parser that constructs an **Abstract Syntax Tree (AST)** representing the structure of the MiniC program.


## The AST Structure
The AST is composed of the following node classes defined in `ast_nodes.py`. 
* **Declarations**: `FuncDecl`, `VarDecl`
* **Statements**: `IfStmt`, `WhileStmt`, `ForStmt`, `ReturnStmt`, `Block`
* **Expressions**: `BinOp`, `Assign`, `FuncCall`, `Id`, `Number`

## `parser.py`
The `parser.py` file contains the `MiniCParser` class, which uses the `sly` library to define the grammar rules for MiniC and constructs the AST nodes accordingly.
You will need to implement the few missing methods in the `MiniCParser` class to handle the various constructs of the MiniC language.
(See the implemented methods for examples of how to construct AST nodes from the parsed tokens.)

You can provide a sample MiniC program to generate the AST: `python parser.py <source.c>`.

## tl;dr
- Implement the missing methods of `MiniCParser` class in `parser.py` using the Python `sly` library.
- Running `make test` should say "All tests passed!".