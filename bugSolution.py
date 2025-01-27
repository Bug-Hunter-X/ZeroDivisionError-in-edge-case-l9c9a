def function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        return 0 # Or raise a more specific exception, e.g., ValueError("Both inputs cannot be zero")
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

#This code handles the case where both a and b are 0
result = function_with_uncommon_error(0,0) 