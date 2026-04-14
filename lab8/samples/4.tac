declare_int_array __s__ 1000
declare_int __sp__ 1
__sp__ = 0
declare_int __ret_val__ 1
label   print_int
declare_int t0 1
declare_int y 1
__sp__ = __sp__ - 1
t0 = __s__[__sp__]
__sp__ = __sp__ - 1
y = __s__[__sp__]
declare_int t1 1
t1 = y < 10
ifFalse t1 goto L0
declare_int t2 1
t2 = y + 48
write t2
goto   L1
label   L0
declare_int last_digit 1
declare_int rem 1
declare_int t3 1
t3 = y / 10
rem = t3
__s__[__sp__] = y
__sp__ = __sp__ + 1
__s__[__sp__] = last_digit
__sp__ = __sp__ + 1
__s__[__sp__] = rem
__sp__ = __sp__ + 1
__s__[__sp__] = t0
__sp__ = __sp__ + 1
__s__[__sp__] = rem
__sp__ = __sp__ + 1
__s__[__sp__] = 2
__sp__ = __sp__ + 1
goto   print_int
label   L2
__sp__ = __sp__ - 1
t0 = __s__[__sp__]
__sp__ = __sp__ - 1
rem = __s__[__sp__]
__sp__ = __sp__ - 1
last_digit = __s__[__sp__]
__sp__ = __sp__ - 1
y = __s__[__sp__]
declare_int t4 1
t4 = __ret_val__
declare_int t5 1
t5 = rem * 10
declare_int t6 1
t6 = y - t5
last_digit = t6
__s__[__sp__] = y
__sp__ = __sp__ + 1
__s__[__sp__] = last_digit
__sp__ = __sp__ + 1
__s__[__sp__] = rem
__sp__ = __sp__ + 1
__s__[__sp__] = t0
__sp__ = __sp__ + 1
__s__[__sp__] = last_digit
__sp__ = __sp__ + 1
__s__[__sp__] = 3
__sp__ = __sp__ + 1
goto   print_int
label   L3
__sp__ = __sp__ - 1
t0 = __s__[__sp__]
__sp__ = __sp__ - 1
rem = __s__[__sp__]
__sp__ = __sp__ - 1
last_digit = __s__[__sp__]
__sp__ = __sp__ - 1
y = __s__[__sp__]
declare_int t7 1
t7 = __ret_val__
label   L1
goto_label L[t0]
label   fibo
declare_int t8 1
declare_int nn 1
__sp__ = __sp__ - 1
t8 = __s__[__sp__]
__sp__ = __sp__ - 1
nn = __s__[__sp__]
declare_int t9 1
t9 = nn <= 1
ifFalse t9 goto L4
__ret_val__ = nn
goto_label L[t8]
goto   L5
label   L4
label   L5
declare_int na 1
declare_int nb 1
__s__[__sp__] = nn
__sp__ = __sp__ + 1
__s__[__sp__] = na
__sp__ = __sp__ + 1
__s__[__sp__] = nb
__sp__ = __sp__ + 1
__s__[__sp__] = t8
__sp__ = __sp__ + 1
declare_int t10 1
t10 = nn - 1
__s__[__sp__] = t10
__sp__ = __sp__ + 1
__s__[__sp__] = 6
__sp__ = __sp__ + 1
goto   fibo
label   L6
__sp__ = __sp__ - 1
t8 = __s__[__sp__]
__sp__ = __sp__ - 1
nb = __s__[__sp__]
__sp__ = __sp__ - 1
na = __s__[__sp__]
__sp__ = __sp__ - 1
nn = __s__[__sp__]
declare_int t11 1
t11 = __ret_val__
na = t11
__s__[__sp__] = nn
__sp__ = __sp__ + 1
__s__[__sp__] = na
__sp__ = __sp__ + 1
__s__[__sp__] = nb
__sp__ = __sp__ + 1
__s__[__sp__] = t8
__sp__ = __sp__ + 1
declare_int t12 1
t12 = nn - 2
__s__[__sp__] = t12
__sp__ = __sp__ + 1
__s__[__sp__] = 7
__sp__ = __sp__ + 1
goto   fibo
label   L7
__sp__ = __sp__ - 1
t8 = __s__[__sp__]
__sp__ = __sp__ - 1
nb = __s__[__sp__]
__sp__ = __sp__ - 1
na = __s__[__sp__]
__sp__ = __sp__ - 1
nn = __s__[__sp__]
declare_int t13 1
t13 = __ret_val__
nb = t13
declare_int t14 1
t14 = na + nb
__ret_val__ = t14
goto_label L[t8]
goto_label L[t8]
label   mod
declare_int t15 1
declare_int p 1
declare_int q 1
__sp__ = __sp__ - 1
t15 = __s__[__sp__]
__sp__ = __sp__ - 1
q = __s__[__sp__]
__sp__ = __sp__ - 1
p = __s__[__sp__]
declare_int t16 1
t16 = p < q
ifFalse t16 goto L8
__ret_val__ = p
goto_label L[t15]
goto   L9
label   L8
label   L9
declare_int quotient 1
declare_int t17 1
t17 = p / q
quotient = t17
declare_int remainder 1
declare_int t18 1
t18 = quotient * q
declare_int t19 1
t19 = p - t18
remainder = t19
__ret_val__ = remainder
goto_label L[t15]
goto_label L[t15]
label   main
declare_int t20 1
declare_int n 1
read n
declare_int t21 1
t21 = n - 48
n = t21
__s__[__sp__] = n
__sp__ = __sp__ + 1
__s__[__sp__] = res
__sp__ = __sp__ + 1
__s__[__sp__] = c
__sp__ = __sp__ + 1
__s__[__sp__] = t20
__sp__ = __sp__ + 1
__s__[__sp__] = n
__sp__ = __sp__ + 1
__s__[__sp__] = 10
__sp__ = __sp__ + 1
goto   print_int
label   L10
__sp__ = __sp__ - 1
t20 = __s__[__sp__]
__sp__ = __sp__ - 1
c = __s__[__sp__]
__sp__ = __sp__ - 1
res = __s__[__sp__]
__sp__ = __sp__ - 1
n = __s__[__sp__]
declare_int t22 1
t22 = __ret_val__
write 32
declare_int res 1
__s__[__sp__] = n
__sp__ = __sp__ + 1
__s__[__sp__] = res
__sp__ = __sp__ + 1
__s__[__sp__] = c
__sp__ = __sp__ + 1
__s__[__sp__] = t20
__sp__ = __sp__ + 1
__s__[__sp__] = n
__sp__ = __sp__ + 1
__s__[__sp__] = 11
__sp__ = __sp__ + 1
goto   fibo
label   L11
__sp__ = __sp__ - 1
t20 = __s__[__sp__]
__sp__ = __sp__ - 1
c = __s__[__sp__]
__sp__ = __sp__ - 1
res = __s__[__sp__]
__sp__ = __sp__ - 1
n = __s__[__sp__]
declare_int t23 1
t23 = __ret_val__
res = t23
__s__[__sp__] = n
__sp__ = __sp__ + 1
__s__[__sp__] = res
__sp__ = __sp__ + 1
__s__[__sp__] = c
__sp__ = __sp__ + 1
__s__[__sp__] = t20
__sp__ = __sp__ + 1
__s__[__sp__] = res
__sp__ = __sp__ + 1
__s__[__sp__] = 12
__sp__ = __sp__ + 1
goto   print_int
label   L12
__sp__ = __sp__ - 1
t20 = __s__[__sp__]
__sp__ = __sp__ - 1
c = __s__[__sp__]
__sp__ = __sp__ - 1
res = __s__[__sp__]
__sp__ = __sp__ - 1
n = __s__[__sp__]
declare_int t24 1
t24 = __ret_val__
write 10
declare_int c 1
__s__[__sp__] = n
__sp__ = __sp__ + 1
__s__[__sp__] = res
__sp__ = __sp__ + 1
__s__[__sp__] = c
__sp__ = __sp__ + 1
__s__[__sp__] = t20
__sp__ = __sp__ + 1
__s__[__sp__] = res
__sp__ = __sp__ + 1
__s__[__sp__] = 26
__sp__ = __sp__ + 1
__s__[__sp__] = 13
__sp__ = __sp__ + 1
goto   mod
label   L13
__sp__ = __sp__ - 1
t20 = __s__[__sp__]
__sp__ = __sp__ - 1
c = __s__[__sp__]
__sp__ = __sp__ - 1
res = __s__[__sp__]
__sp__ = __sp__ - 1
n = __s__[__sp__]
declare_int t25 1
t25 = __ret_val__
declare_int t26 1
t26 = 65 + t25
c = t26
write c
__ret_val__ = 0