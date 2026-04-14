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
label   add
declare_int t8 1
declare_int a 1
declare_int b 1
__sp__ = __sp__ - 1
t8 = __s__[__sp__]
__sp__ = __sp__ - 1
b = __s__[__sp__]
__sp__ = __sp__ - 1
a = __s__[__sp__]
declare_int t9 1
t9 = a + b
__ret_val__ = t9
goto_label L[t8]
goto_label L[t8]
label   main
declare_int t10 1
declare_int result 1
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = t10
__sp__ = __sp__ + 1
__s__[__sp__] = 13
__sp__ = __sp__ + 1
__s__[__sp__] = 7
__sp__ = __sp__ + 1
__s__[__sp__] = 4
__sp__ = __sp__ + 1
goto   add
label   L4
__sp__ = __sp__ - 1
t10 = __s__[__sp__]
__sp__ = __sp__ - 1
result = __s__[__sp__]
declare_int t11 1
t11 = __ret_val__
result = t11
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = t10
__sp__ = __sp__ + 1
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = 5
__sp__ = __sp__ + 1
goto   print_int
label   L5
__sp__ = __sp__ - 1
t10 = __s__[__sp__]
__sp__ = __sp__ - 1
result = __s__[__sp__]
declare_int t12 1
t12 = __ret_val__
__ret_val__ = 0