N, M = map(int, input().split()) #맵 크기 입력
tile = [] # 타일 맵 생성
count = 0

# 타일 입력
for i in range(0,N):
    arr = list(input())
    tile.append(arr)

# 타일 방문 확인
visited = [[False] * M for _ in range(N)]

def DFS(x,y):
    visited[x][y] = True
    if tile[x][y] == '|' :
        if x + 1 < N and tile[x+1][y] == '|' and visited[x+1][y] == False:
            DFS(x+1, y)
        else :
            return
    if tile[x][y] == '-':
        if y+1 < M and tile[x][y + 1] == '-' and visited[x][y + 1] == False:
            DFS(x,y+1)
        else:
            return
        
for i in range(0,N):
    for j in range(0,M):
        if visited[i][j] == False:
            DFS(i,j)        
            count += 1

print(count)