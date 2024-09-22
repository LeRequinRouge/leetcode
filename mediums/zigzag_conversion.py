s1 = 'PAYPALISHIRING'
# s2 = 'AB'
num_rows1 = 3
num_rows2 = 4


def convert_zigzag(s, rows):
    row_dict = {}
    counter = 0
    converted_string = ''

    if len(s) == 1:
        return s

    # initialize the row dictionary
    for row in range(rows):
        row_dict[row] = ''
        print(row_dict)

    # initialize a flag to keep track of a reverse in iteration.
    reverse_flag = False

    # for loop in range of the length of the string to section out the substrings.
    for i in range(len(s)):
        # counter is the key and the current character is added to the row in the dictionary.
        row_dict[counter] += s[i]
        # counter is incremented if the reverse flag is False.
        if not reverse_flag:
            counter += 1
        # counter is decremented if the reverse flag is True.
        else:
            counter -= 1
        # reverse flag is set to False if the counter decrements to zero
        if counter == 0:
            reverse_flag = False
        # reverse flag is set to True if the counter reaches the maximum number of rows.
        elif counter == rows - 1:
            reverse_flag = True

    # substrings within the dictionary are added together for the final zigzag result.
    for key in row_dict.keys():
        converted_string += row_dict[key]
    return converted_string


convert_zigzag(s1, num_rows1)
convert_zigzag(s1, num_rows2)
# convert_zigzag(s2, 1)