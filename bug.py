def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

#This code will produce a ZeroDivisionError if both a and b are 0.
result = function_with_uncommon_error(0,0)