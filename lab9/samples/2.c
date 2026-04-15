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

int sq(int x) {
    return x * x;
}

void main() {
    int input;
    int count;
    count = 0;

    read(input);
    input = input - 48; // Convert ASCII to integer

    print_int(sq(input));

}