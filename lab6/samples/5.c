#include<1.c>   //can include arbirary .c files 


//recursive function to calculate
//nth Fibonacci number
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