# hacky brute force way of finding the longest palindromic substring in a string
s1 = 'a'
s2 = 'ac'
s3 = 'babad'
s4 = 'cbbd'
s5 = 'ccc'


def find_palindrome(s):
    longest_palindromic_substring = ''
    substring = ''
    palindromic_substring = ''

    # for loop within the range of the string.
    for i in range(len(s)):
        # taking note of the initial character of the substring.
        current_head = s[i]
        substring += current_head
        # brute force nested for loop to iterate through the values AFTER the current_head character.
        for c in range(i + 1, len(s)):
            # if the current character doesn't equal the head then add it to the substring.
            if s[c] != current_head:
                substring += s[c]
            # if the current character DOES equal the head then add it to the substring and check for palindrome.
            elif s[c] == current_head:
                substring += current_head
                if substring == substring[::-1]:
                    palindromic_substring = substring
        # if the substring is the same forwards as it is reversed then it's a palindrome.
        if substring == substring[::-1]:
            palindromic_substring = substring
        # if the length of the found palindrome is higher than the current longest then the longest palindrome
        # is set to the found palindrome.
        if len(palindromic_substring) > len(longest_palindromic_substring):
            longest_palindromic_substring = palindromic_substring
        # destroy the substring for use in future iteration
        substring = ''
    print(f"The longest palindromic substring of '{s}' is '{longest_palindromic_substring}'")


find_palindrome(s1)
find_palindrome(s2)
find_palindrome(s3)
find_palindrome(s4)
find_palindrome(s5)