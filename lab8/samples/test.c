int fibo(int n) {
    if (n <= 1) {
        return n;
    }
    return fibo(n - 1) + fibo(n - 2);
}
int main() {
    write(fibo(5));
    return 0;
}