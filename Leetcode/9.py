def isPalindrome(x):
    x = str(x)
    y=x[::-1]
    return x == y


x = 10
print(isPalindrome(x))
