def changetwo(binary_str):
    result = 0
    num = len(binary_str)
    for i in range(len(binary_str)):
        result += int(binary_str[i]) * 2 ** (num - 1)
        num -= 1
    return result

N = input()

num = changetwo(N)
num = num * 17

binary_result = bin(num)[2:]
print(binary_result)