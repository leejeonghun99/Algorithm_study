from collections import deque

N = int(input())

for i in range(N):
    arr = list(map(str, input()))
    isTrue = False
    test = deque()
    for i in range(len(arr)):
        if arr[i] == '(':
            test.append(True)
        else:
            if len(test) == 0:
                isTrue = True
                break
            test.pop()
    if len(test) > 0 or isTrue == True:
        print("NO")
    else:
        print("YES")