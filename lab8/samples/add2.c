int dbl(int x) {
    return x*2;
}

int sq(int z) {
    return z*z;
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

int main() {
    int result;
    result = dbl(13);
    print_int(result);
    write(10); // Newline for better readability
    result = sq(13);
    print_int(result);
    write(10); // Newline for better readability
    int mod_result;
    mod_result = mod(13, 5);
    print_int(mod_result);
    write(10); // Newline for better readability
    return 0;
}