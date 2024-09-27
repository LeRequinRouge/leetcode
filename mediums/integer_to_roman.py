# this program converts an integer value to roman numeral.
number1 = 3749
number2 = 58
number3 = 1994
number4 = 47


def int_to_roman(num):
    # converts the given num into a string for future manipulation.
    string_num = str(num)
    roman_conversion = ''
    counter = 0
    # dictionary containing roman numeral conversion keys.
    roman_dict = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    # loops through the characters of int-turned-string value
    for c in string_num:
        temp_num = c
        # for loop that appends a '0' character to temp_num string depending on the length of given number
        # subtracted by a counter used to mimic the current index of c in string_num.
        for i in range(len(string_num) - counter - 1):
            temp_num += '0'
        # the temporary num string is then converted into an int for arithmetic manipulation.
        temp_num = int(temp_num)
        counter += 1

        # loops until temp_num is 0
        while temp_num != 0:
            # iterates through the dictionary until a value can be subtracted from temp_num
            # and a conversion symbol appended to the roman_conversion string. The loop is then broken.
            for key, value in roman_dict.items():
                if temp_num >= value:
                    roman_conversion += key
                    temp_num -= value
                    break

    return roman_conversion


print(int_to_roman(number1))
print(int_to_roman(number2))
print(int_to_roman(number3))
print(int_to_roman(number4))