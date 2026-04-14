int x;
int y;
char c;

void main() {
    x = 10;
    y = 20;
    c = 'A';
    int result;
    int ascii_zero;
    ascii_zero = 48; // ASCII value of '0'
    result = (x + y) * 2 / 5;
    result = result - 5;
    result = result + ascii_zero; // Convert to ASCII character
    write(result);
}