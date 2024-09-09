import sys 
sys.setrecursionlimit(10000)

N = int(input())

normalVisited = [[False] * N for _ in range(N)]
rgVisited = [[False] * N for _ in range(N)]
normalCnt = 0
rgCnt = 0
rgbMap = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(N):
    arr = list(input())
    rgbMap.append(arr)

def RGBDFS(x,y):
    normalVisited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if rgbMap[nx][ny] == nowColor and normalVisited[nx][ny] == False:
                normalVisited[nx][ny] = True
                RGBDFS(nx, ny)

def RGDFS(x,y):
    rgVisited[x][y] = True
    if nowColor == 'R' or nowColor == 'G':
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if (rgbMap[nx][ny] == 'R' or rgbMap[nx][ny] == 'G') and rgVisited[nx][ny] == False:
                    rgVisited[nx][ny] = True
                    RGDFS(nx, ny)
    else :
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if rgbMap[nx][ny] == 'B' and rgVisited[nx][ny] == False:
                    rgVisited[nx][ny] = True
                    RGDFS(nx, ny)

for i in range(N):
    for j in range(N):
        if (normalVisited[i][j] == False):
            nowColor = rgbMap[i][j]
            RGBDFS(i, j)
            normalCnt += 1
        if (rgVisited[i][j] == False):
            nowColor = rgbMap[i][j]
            RGDFS(i, j)
            rgCnt += 1


print(normalCnt,rgCnt)