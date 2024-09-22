num1 = -321
num2 = 120


def reverse_integer(x):
    reversal = 0

    # if given integer is negative, convert the absolute value of the integer into a string.
    # reassign the negative through the -abs() method after converting the reversed string into an int.
    if x < 0:
        convert = str(abs(x))
        reversal = -abs(int(convert[::-1]))
    # if positive, convert the value to a string, reverse it, then convert back to an int.
    else:
        convert = str(x)
        reversal = int(convert[::-1])

    # return the reversed value if it does not exceed the 32-bit integer range.
    # otherwise return 0
    if -pow(2, 31) <= reversal <= pow(2, 31) - 1:
        return reversal
    else:
        return 0


reversed_int = reverse_integer(num2)
print(reversed_int)