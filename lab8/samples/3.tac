declare_int_array __s__ 1000
declare_int __sp__ 1
__sp__ = 0
declare_int __ret_val__ 1
declare_int_array arr 10
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
label   print_arr
declare_int t8 1
__sp__ = __sp__ - 1
t8 = __s__[__sp__]
declare_int i 1
i = 0
label   L4
declare_int t9 1
t9 = i < 10
ifFalse t9 goto L5
__s__[__sp__] = i
__sp__ = __sp__ + 1
__s__[__sp__] = t8
__sp__ = __sp__ + 1
declare_int t10 1
t10 = arr[i]
__s__[__sp__] = t10
__sp__ = __sp__ + 1
__s__[__sp__] = 6
__sp__ = __sp__ + 1
goto   print_int
label   L6
__sp__ = __sp__ - 1
t8 = __s__[__sp__]
__sp__ = __sp__ - 1
i = __s__[__sp__]
declare_int t11 1
t11 = __ret_val__
write 32
declare_int t12 1
t12 = i + 1
i = t12
goto   L4
label   L5
goto_label L[t8]
label   main
declare_int t13 1
__s__[__sp__] = j
__sp__ = __sp__ + 1
__s__[__sp__] = t13
__sp__ = __sp__ + 1
__s__[__sp__] = 7
__sp__ = __sp__ + 1
goto   print_arr
label   L7
__sp__ = __sp__ - 1
t13 = __s__[__sp__]
__sp__ = __sp__ - 1
j = __s__[__sp__]
declare_int t14 1
t14 = __ret_val__
write 10
declare_int j 1
j = 0
label   L8
declare_int t15 1
t15 = j < 10
ifFalse t15 goto L9
declare_int t16 1
t16 = j * j
arr[j] = t16
declare_int t17 1
t17 = j + 1
j = t17
goto   L8
label   L9
__s__[__sp__] = j
__sp__ = __sp__ + 1
__s__[__sp__] = t13
__sp__ = __sp__ + 1
__s__[__sp__] = 10
__sp__ = __sp__ + 1
goto   print_arr
label   L10
__sp__ = __sp__ - 1
t13 = __s__[__sp__]
__sp__ = __sp__ - 1
j = __s__[__sp__]
declare_int t18 1
t18 = __ret_val__
write 10