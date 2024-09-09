from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def BFS():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and tomato[nx][ny] == 0:
                visited[nx][ny] = True
                tomato[nx][ny] = tomato[a][b] + 1
                queue.append([nx,ny])


M, N = map(int, input().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i,j])
BFS()
answer = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            answer = 0
            print(-1)
            exit(0)
        answer = max(answer, tomato[i][j])
print(answer - 1)