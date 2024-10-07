import sys
input = sys.stdin.readline

N = int(input())

arr = [[0 for _ in range(2)] for _ in range(N + 1)]

arr[1][1] = 1
arr[1][0] = 0

for i in range(2, N + 1):
    arr[i][0] = arr[i - 1][0] + arr[i - 1][1]
    arr[i][1] = arr[i - 1][0]
print(arr[N][0] + arr[N][1])