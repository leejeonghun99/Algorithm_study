n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

for _ in range(m):
    num = arr[0] + arr[1]
    arr[0] = num
    arr[1] = num
    arr.sort()

print(sum(arr))