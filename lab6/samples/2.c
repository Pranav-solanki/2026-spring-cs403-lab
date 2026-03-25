#include<1.c>
void main() {
    int input;
    int count;
    count = 0;

    read(input);

    while (count < input) {
        if (count % 2 == 0) {
            write(count);
        } else {
            // Do nothing
        }
        count = count + 1;
    }
}