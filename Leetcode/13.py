def romanToInt(s):
    length = len(s)
    s_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    index = 0
    result = 0
    while index < length:
        if s[index] == 'I':
            if index==length-1:
                result += 1
                index += 1
            else:
                if s[index + 1] == 'V':
                    result += 4
                    index += 2
                elif s[index + 1] == 'X':
                    result += 9
                    index += 2
                else:
                    result += 1
                    index += 1
        elif s[index] == 'X':
            if index == length - 1:
                result += 10
                index += 1
            else:
                if s[index + 1] == 'L':
                    result += 40
                    index += 2
                elif s[index + 1] == 'C':
                    result += 90
                    index += 2
                else:
                    result += 10
                    index += 1
        elif s[index] == 'C':
            if index == length - 1:
                result += 100
                index += 1
            else:
                if s[index + 1] == 'D':
                    result += 400
                    index += 2
                elif s[index + 1] == 'M':
                    result += 900
                    index += 2
                else:
                    result += 100
                    index += 1
        else:
            result += s_n[s[index]]
            index+=1

    return result


s = "MCMXCIV"
print(romanToInt(s))
