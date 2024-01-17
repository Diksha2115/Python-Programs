def is_palindrome(s):
    return s == s[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")
