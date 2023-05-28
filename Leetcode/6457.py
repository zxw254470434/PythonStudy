def removeTrailingZeros(num):
    return num.rstrip('0')


num = '123'
print(type(removeTrailingZeros(num)))
print(removeTrailingZeros(num))
