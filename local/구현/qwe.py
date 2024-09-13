N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

K = int(input())
for i in range(K):
    answer = 0
    fx, fy, lx, ly = map(int, input().split())
    for j in range(fx - 1, lx):
        for k in range(fy - 1, ly):
            answer += arr[j][k]
    print(answer)
