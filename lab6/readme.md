# Lab 6: MiniC Lexer
In Labs 1-5 we have implemented an Assembler for the SIC architecture, which translates SIC assembly language into machine code.
Now, we start building a Compiler for a (kind-of) subset of the C language, that we call MiniC.

The first phase of a compiler is Lexical Analysis, where the Lexer reads the source code as character-stream and outputs a stream of tokens.

## Task
In this lab, implement the missing methods of `MiniCLexer` class in `lexer.py` using the Python `sly` library.[^sly]
It should correctly tokenize the provided MiniC source files in `samples/` and pass all the tests in `make test`.

[^sly]: SLY (Sly Lex Yacc) is a Python library for writing lexers and parsers. It is a modern alternative that can be installed in your virtual environment using `pip install sly`.

## MiniC Language Specification
The MiniC language supports the following features:
- Basic data types: `int`, `char`, `void` (and their pointers)
- Variable declarations, both global and local (e.g., `int x;`)
- Function definitions (e.g., `void foo() { ... }`)
- Control flow statements: `if`, `else`, `while`, `return`, `goto` (no `for` loops)
- I/O: `read()`, `write()`
- Preprocessor directive: `#include` (In future, we will add more decorators like @cache, @inline etc.)
- Comments: Single-line (`// ...`) and multi-line (`/* ... */`)
- Literals (e.g., `"Hello, World!"`, `'a'`, `123`, `007`)
- Standard operators and seperators: `+`, `-`, `*`, `/`, `=`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `&&`, `||`, `!`, `(`, `)`, `{`, `}`, `[`, `]`, `;`, `,`
- Whitespaces are ignored

## Sample MiniC Code
```c
#include<1.c> 
//can include arbirary .c files 


/* recursive function to calculate
nth Fibonacci number */
int fibo(int n) {
    if (n <= 1) {
        return n;
    }
    return fibo(n - 1) + fibo(n - 2);
}

int main() {
    int n;
    /*  write is a built-in function to 
    print strings/int/char to console  */
    write("Enter n");   //
    read(n);
    write(n);
    write("th Fibonacci number is");
    int res;
    res = fibo(n);
    write(res);
    print("\nIts favorite character is");
    char c;
    c = 'A' + (res % 26);
    print(c);
    return 0;
}
```



## tl;dr
- Implement the `MiniCLexer` class in `lexer.py` using the SLY library.
- Running `make test` should say "All tests passed!".

