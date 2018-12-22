# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?


def is_palindrome2(s):

	if len(s) <= 1:
		return True

    for i in range(0, len(s) / 2):
        if s[i] != s[-(i + 1)]:
            return False
        return True


print(is_palindrome2('a'))

