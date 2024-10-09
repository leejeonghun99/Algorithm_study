N, M = map(int, input().split())

arr = [[0] * (N + 1)]
arr2 = [[0] * (N + 1) for _ in range( N + 1)]

for _ in range(N):
    a = [0] + [int(x) for x in input().split()]
    arr.append(a)

for i in range(1,N + 1):
    for j in range(1, N + 1):
        arr2[i][j] = arr2[i][j-1] + arr2[i-1][j] - arr2[i-1][j-1] + arr[i][j]
    


for i in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    answer = arr2[x2][y2] - arr2[x1-1][y2] - arr2[x2][y1-1] + arr2[x1 - 1][y1 - 1]
    print(answer)