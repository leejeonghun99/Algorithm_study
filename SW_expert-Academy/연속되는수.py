N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

max_num = 0

def count(exclude_num):
    global max_num
    current_len = 0
    max_len = 0
    previous_num = None

    for num in arr:
        if num == exclude_num:
            continue
        if num == previous_num:
            current_len += 1
        else:
            previous_num = num
            current_len = 1
        max_len = max(max_len, current_len)

    max_num = max(max_num, max_len)

for i in range(N):
    count(arr[i])

print(max_num)
