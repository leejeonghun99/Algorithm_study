a = input()
b = input()

arr = []
arr2 = []

# 2진수를 10진수로 변환
def changetwo(binary_str):
    result = 0
    num = len(binary_str)
    for i in range(len(binary_str)):
        result += int(binary_str[i]) * 2 ** (num - 1)
        num -= 1
    return result

def changethree(binary_str):
    result = 0
    num = len(binary_str)
    for i in range(len(binary_str)):
        result += int(binary_str[i]) * 3 ** (num - 1)
        num -= 1
    return result

# 입력된 문자열을 리스트로 변환
a_list = list(a)
b_list = list(b)



# 각 자리의 비트를 뒤집고, 10진수로 변환하여 arr에 추가
for i in range(len(a_list)):
    # 비트를 뒤집음
    if a_list[i] == '0':
        a_list[i] = '1'
        modified_binary = ''.join(a_list)
        decimal_value = changetwo(modified_binary)
        arr.append(decimal_value)
        a_list[i] = '0'
    else:
        a_list[i] = '0'
        modified_binary = ''.join(a_list)
        decimal_value = changetwo(modified_binary)
        arr.append(decimal_value)
        a_list[i] = '1'
    
    # 뒤집은 후의 리스트를 문자열로 변환하여 10진수로 변환
    
for i in range(len(b_list)):
    if b_list[i] == '0':
        b_list[i] = '1'
        modified_binary = ''.join(b_list)
        decimal_value = changethree(modified_binary)
        arr2.append(decimal_value)
        b_list[i] = '2'
        modified_binary = ''.join(b_list)
        decimal_value = changethree(modified_binary)
        arr2.append(decimal_value)
        b_list[i] = '0'
    elif b_list[i] == '1':
        b_list[i] = '0'
        modified_binary = ''.join(b_list)
        decimal_value = changethree(modified_binary)
        arr2.append(decimal_value)
        b_list[i] = '2'
        modified_binary = ''.join(b_list)
        decimal_value = changethree(modified_binary)
        arr2.append(decimal_value)
        b_list[i] = '1'
    else :
        b_list[i] = '0'
        modified_binary = ''.join(b_list)
        decimal_value = changethree(modified_binary)
        arr2.append(decimal_value)
        b_list[i] = '1'
        modified_binary = ''.join(b_list)
        decimal_value = changethree(modified_binary)
        arr2.append(decimal_value)
        b_list[i] = '2'

arr = sorted(arr)
arr2 = sorted(arr2)

start1 = 0
start2 = 0

while True:
    if arr[start1] > arr2[start2]:
        start2 += 1
    elif arr[start1] < arr2[start2]:
        start1 += 1
    else:
        break

print(arr[start1])