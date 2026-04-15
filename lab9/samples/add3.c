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

int add(int a, int b) {
    return a + b;
}

int main() {
    int result;
    result = add(13, 7);
    print_int(result);
    return 0;
}