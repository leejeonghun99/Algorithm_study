import sys 
sys.setrecursionlimit(10000)
T = int(input())
dx = [1, -1 , 0, 0]
dy = [0, 0, 1, -1]
for _ in range(0,T):
    M, N, K = map(int, input().split())

    visited = [[False] * M for _ in range(N)]
    count = 0
    farm = [[0] * M for _ in range(N)]

    def DFS(x,y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if farm[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    DFS(nx,ny)

        

    for i in range(0,K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    for i in range(0,N):
        for j in range(0,M):
            if farm[i][j] == 1 and visited[i][j] == False:
                DFS(i,j)
                count += 1
    print(count)    