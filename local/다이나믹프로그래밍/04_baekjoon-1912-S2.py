n = int(input())

arr = list(map(int, input().split()))

arr2 = [0] * (n + 1)

if n > 2:
    arr2[1] = arr[0]
    arr2[2] = max(arr[1], arr[0] + arr[1])
    for i in range(3, n + 1):
        arr2[i] = max(arr2[i - 1] + arr[i - 1] , arr[i - 1] )
    print(max(arr2[1:]))
elif n == 2:
    a = arr[0]
    b = arr[1]
    print(max(a, b, a + b))
else:
    print(arr[0])