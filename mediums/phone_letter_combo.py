# solution obtained via
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/5125020/video-simple-solution
digit_str = '23'


def find_combo(digits):
    if not digits:
        return []

    combo_list = []
    combo_dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(index, combo):
        if index == len(digits):
            combo_list.append(combo)
            return

        for value in combo_dict[digits[index]]:
            backtrack(index + 1, combo + value)

    backtrack(0, '')
    return combo_list


if __name__ == '__main__':
    print(find_combo(digit_str))