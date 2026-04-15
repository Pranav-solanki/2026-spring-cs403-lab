int arr[10];

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

void print_arr() {
    int i;
    i = 0;
    while (i < 10) {
        print_int(arr[i]);
        write(32);
        i = i + 1;
    }
}

void main() {
    print_arr();
    write(10);
    int j;
    j = 0;
    while (j < 10) {
        arr[j] = j * j;
        j = j + 1;
    }
    print_arr();
    write(10);
}