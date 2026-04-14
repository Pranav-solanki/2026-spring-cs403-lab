declare_int_array __s__ 1000
declare_int __sp__ 1
__sp__ = 0
declare_int __ret_val__ 1
label   dbl
declare_int t0 1
declare_int x 1
__sp__ = __sp__ - 1
t0 = __s__[__sp__]
__sp__ = __sp__ - 1
x = __s__[__sp__]
declare_int t1 1
t1 = x * 2
__ret_val__ = t1
goto_label L[t0]
goto_label L[t0]
label   sq
declare_int t2 1
declare_int z 1
__sp__ = __sp__ - 1
t2 = __s__[__sp__]
__sp__ = __sp__ - 1
z = __s__[__sp__]
declare_int t3 1
t3 = z * z
__ret_val__ = t3
goto_label L[t2]
goto_label L[t2]
label   mod
declare_int t4 1
declare_int p 1
declare_int q 1
__sp__ = __sp__ - 1
t4 = __s__[__sp__]
__sp__ = __sp__ - 1
q = __s__[__sp__]
__sp__ = __sp__ - 1
p = __s__[__sp__]
declare_int t5 1
t5 = p < q
ifFalse t5 goto L0
__ret_val__ = p
goto_label L[t4]
goto   L1
label   L0
label   L1
declare_int quotient 1
declare_int t6 1
t6 = p / q
quotient = t6
declare_int remainder 1
declare_int t7 1
t7 = quotient * q
declare_int t8 1
t8 = p - t7
remainder = t8
__ret_val__ = remainder
goto_label L[t4]
goto_label L[t4]
label   print_int
declare_int t9 1
declare_int y 1
__sp__ = __sp__ - 1
t9 = __s__[__sp__]
__sp__ = __sp__ - 1
y = __s__[__sp__]
declare_int t10 1
t10 = y < 10
ifFalse t10 goto L2
declare_int t11 1
t11 = y + 48
write t11
goto   L3
label   L2
declare_int last_digit 1
declare_int rem 1
declare_int t12 1
t12 = y / 10
rem = t12
__s__[__sp__] = y
__sp__ = __sp__ + 1
__s__[__sp__] = last_digit
__sp__ = __sp__ + 1
__s__[__sp__] = rem
__sp__ = __sp__ + 1
__s__[__sp__] = t9
__sp__ = __sp__ + 1
__s__[__sp__] = rem
__sp__ = __sp__ + 1
__s__[__sp__] = 4
__sp__ = __sp__ + 1
goto   print_int
label   L4
__sp__ = __sp__ - 1
t9 = __s__[__sp__]
__sp__ = __sp__ - 1
rem = __s__[__sp__]
__sp__ = __sp__ - 1
last_digit = __s__[__sp__]
__sp__ = __sp__ - 1
y = __s__[__sp__]
declare_int t13 1
t13 = __ret_val__
declare_int t14 1
t14 = rem * 10
declare_int t15 1
t15 = y - t14
last_digit = t15
__s__[__sp__] = y
__sp__ = __sp__ + 1
__s__[__sp__] = last_digit
__sp__ = __sp__ + 1
__s__[__sp__] = rem
__sp__ = __sp__ + 1
__s__[__sp__] = t9
__sp__ = __sp__ + 1
__s__[__sp__] = last_digit
__sp__ = __sp__ + 1
__s__[__sp__] = 5
__sp__ = __sp__ + 1
goto   print_int
label   L5
__sp__ = __sp__ - 1
t9 = __s__[__sp__]
__sp__ = __sp__ - 1
rem = __s__[__sp__]
__sp__ = __sp__ - 1
last_digit = __s__[__sp__]
__sp__ = __sp__ - 1
y = __s__[__sp__]
declare_int t16 1
t16 = __ret_val__
label   L3
goto_label L[t9]
label   main
declare_int t17 1
declare_int result 1
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = mod_result
__sp__ = __sp__ + 1
__s__[__sp__] = t17
__sp__ = __sp__ + 1
__s__[__sp__] = 13
__sp__ = __sp__ + 1
__s__[__sp__] = 6
__sp__ = __sp__ + 1
goto   dbl
label   L6
__sp__ = __sp__ - 1
t17 = __s__[__sp__]
__sp__ = __sp__ - 1
mod_result = __s__[__sp__]
__sp__ = __sp__ - 1
result = __s__[__sp__]
declare_int t18 1
t18 = __ret_val__
result = t18
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = mod_result
__sp__ = __sp__ + 1
__s__[__sp__] = t17
__sp__ = __sp__ + 1
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = 7
__sp__ = __sp__ + 1
goto   print_int
label   L7
__sp__ = __sp__ - 1
t17 = __s__[__sp__]
__sp__ = __sp__ - 1
mod_result = __s__[__sp__]
__sp__ = __sp__ - 1
result = __s__[__sp__]
declare_int t19 1
t19 = __ret_val__
write 10
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = mod_result
__sp__ = __sp__ + 1
__s__[__sp__] = t17
__sp__ = __sp__ + 1
__s__[__sp__] = 13
__sp__ = __sp__ + 1
__s__[__sp__] = 8
__sp__ = __sp__ + 1
goto   sq
label   L8
__sp__ = __sp__ - 1
t17 = __s__[__sp__]
__sp__ = __sp__ - 1
mod_result = __s__[__sp__]
__sp__ = __sp__ - 1
result = __s__[__sp__]
declare_int t20 1
t20 = __ret_val__
result = t20
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = mod_result
__sp__ = __sp__ + 1
__s__[__sp__] = t17
__sp__ = __sp__ + 1
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = 9
__sp__ = __sp__ + 1
goto   print_int
label   L9
__sp__ = __sp__ - 1
t17 = __s__[__sp__]
__sp__ = __sp__ - 1
mod_result = __s__[__sp__]
__sp__ = __sp__ - 1
result = __s__[__sp__]
declare_int t21 1
t21 = __ret_val__
write 10
declare_int mod_result 1
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = mod_result
__sp__ = __sp__ + 1
__s__[__sp__] = t17
__sp__ = __sp__ + 1
__s__[__sp__] = 13
__sp__ = __sp__ + 1
__s__[__sp__] = 5
__sp__ = __sp__ + 1
__s__[__sp__] = 10
__sp__ = __sp__ + 1
goto   mod
label   L10
__sp__ = __sp__ - 1
t17 = __s__[__sp__]
__sp__ = __sp__ - 1
mod_result = __s__[__sp__]
__sp__ = __sp__ - 1
result = __s__[__sp__]
declare_int t22 1
t22 = __ret_val__
mod_result = t22
__s__[__sp__] = result
__sp__ = __sp__ + 1
__s__[__sp__] = mod_result
__sp__ = __sp__ + 1
__s__[__sp__] = t17
__sp__ = __sp__ + 1
__s__[__sp__] = mod_result
__sp__ = __sp__ + 1
__s__[__sp__] = 11
__sp__ = __sp__ + 1
goto   print_int
label   L11
__sp__ = __sp__ - 1
t17 = __s__[__sp__]
__sp__ = __sp__ - 1
mod_result = __s__[__sp__]
__sp__ = __sp__ - 1
result = __s__[__sp__]
declare_int t23 1
t23 = __ret_val__
write 10
__ret_val__ = 0