def string_to_integer(s):
    new_string = ''
    converted_value = ''
    negative_flag = False
    positive_flag = False

    # loop to iterate through characters of a string to filter through initial
    # white space, determine sign (+/-), and only add digits until 'c' is a non-digit
    # character or the end of the loop is met.
    for c in s:
        if c == ' ' and new_string == '' and not negative_flag and not positive_flag:
            pass
        elif c == '+' and not negative_flag and not positive_flag:
            positive_flag = True
        elif c == '-' and new_string == '' and not positive_flag and not negative_flag:
            negative_flag = True
        elif c.isdigit():
            new_string += c
            # if a digit is found before a sign, the positive flag is tripped.
            if not positive_flag and not negative_flag:
                positive_flag = True
        else:
            break

    # if the new string is empty due to an early break in the for loop, return 0
    if new_string == '':
        return 0
    # if a negative sign was detected the flag will be tripped and the conversion will
    # include a negative value.
    elif negative_flag:
        converted_value = -int(new_string)
    else:
        converted_value = int(new_string)

    # rounding to the lowest 32-bit integer if it's beyond or above.
    if converted_value < -pow(2, 31):
        return -pow(2, 31)
    elif converted_value > pow(2, 31) - 1:
        return pow(2, 31) - 1
    else:
        return converted_value


test_value = string_to_integer('42')
print(test_value)

