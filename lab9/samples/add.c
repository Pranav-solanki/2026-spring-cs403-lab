int main() {
    int n;
    n = 10;
    int i;
    i = 1;
    int sum;
    sum = 0;
    int ascii_zero;
    ascii_zero = 48; // ASCII value of '0'
    while(i < n) {
        sum = sum + i;
        i = i + 1;
    }
    int first_digit;
    first_digit = sum / 10;
    int second_digit;
    second_digit = sum - (first_digit * 10);
    write(first_digit + ascii_zero);
    write(second_digit + ascii_zero);
    int x;
    return 0;
}