int stack[1000];
int sp;
int jump_table[5];

// this is a sample program to demonstrate the "Computed Goto" construct in C.
/*
    The "Computed Goto" construct allows you to jump to a label based on the value of a variable. ... ...   ..      ..
*/

void main() {
    int target;
    sp = 0;
    
    // Push a value
    stack[sp] = 42;
    sp = sp + 1;

    target = 2;
    
    // The "Computed Goto" construct
    // Your lexer must see: GOTO, ID(jump_table), LBRACKET, ID(target), RBRACKET, SEMI
    goto jump_table[target];

    LABEL1:
        write(1);
        return;
    
    LABEL2:
        write(2);
        return;
}