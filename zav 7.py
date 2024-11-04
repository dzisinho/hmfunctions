def is_palindrome(num):
    num = str(num)
    return num == num[::-1]
print(is_palindrome(12321))