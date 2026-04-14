declare_int_array __s__ 1000
declare_int __sp__ 1
__sp__ = 0
declare_int __ret_val__ 1
declare_int x 1
declare_int y 1
declare_char c 1
label   main
declare_int t0 1
x = 10
y = 20
c = 'A'
declare_int result 1
declare_int ascii_zero 1
ascii_zero = 48
declare_int t1 1
t1 = x + y
declare_int t2 1
t2 = t1 * 2
declare_int t3 1
t3 = t2 / 5
result = t3
declare_int t4 1
t4 = result - 5
result = t4
declare_int t5 1
t5 = result + ascii_zero
result = t5
write result