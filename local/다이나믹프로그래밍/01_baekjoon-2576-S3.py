N = int(input())

arr = [0] * 301

for i in range(N):
    arr[i + 1] = int(input())

arr2 = [0] * 301
arr2[1] = arr[1]
arr2[2] = arr[1] + arr[2]
arr2[3] = max(arr[1] + arr[3], arr[2] + arr[3])

for i in range(4, N + 1):
    arr2[i] = max(arr2[i - 3] + arr[i - 1] + arr[i], arr2[i - 2] + arr[i])
print(arr2[N])

