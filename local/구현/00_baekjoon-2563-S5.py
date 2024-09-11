N = int(input())
visited = [[0 for _ in range(100)] for _ in range(100)]
count = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            if visited[i][j] == 0:
                visited[i][j] = 1
                count += 1
print(count)