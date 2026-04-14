#include<1.c>   //can include arbirary .c files 

int print_int(int y) {
    if(y < 10) {
        write(y + 48);
    } else {
        int last_digit;
        int rem;
        rem = y / 10;
        print_int(rem);
        last_digit = (y - rem * 10);
        print_int(last_digit);
    }
}

//recursive function to calculate
//nth Fibonacci number
int fibo(int nn) {
    if (nn <= 1) {
        return nn;
    }
    int na;
    int nb;
    na = fibo(nn - 1);
    nb = fibo(nn - 2);
    return na + nb;
}

int mod(int p, int q) {
    if (p < q) {
        return p; // If p is less than q, return p as the result
    }
    int quotient;
    quotient = p / q; // Integer division to get the quotient
    int remainder;
    remainder = p - (quotient * q); // Calculate the remainder
    return remainder; // Return the remainder as the result
}

int main() {
    int n;
    /*  write is a built-in function to 
    print strings/int/char to console  */
    read(n);
    n = n - 48; // Convert ASCII character to integer
    print_int(n);
    write(32); // Print a space
    int res;
    res = fibo(n);
    print_int(res);
    write(10); // Print a newline
    int c;
    c = 65 + mod(res, 26); // Get a character based on the Fibonacci result
    write(c);
    return 0;
}