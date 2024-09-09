p, q = map(int,input().split())
half = p // 2
arr = []
for i in range(1, half+1):
    if (p % i == 0):
        if(i not in arr):
            arr.append(i)
        if(int(p / i) not in arr):
            arr.append(int(p / i))

arr = sorted(arr)
if(q <= len(arr)):
    print(arr[q-1])
else:
    print(0)