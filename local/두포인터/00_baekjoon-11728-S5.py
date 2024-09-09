N, M = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr3 = []

num = max(N, M)

for i in range(num):
    if(N > i):
        arr3.append(arr1[i])
    if(M > i):
        arr3.append(arr2[i])

arr3 = sorted(arr3)
print(" ".join(map(str, arr3)))