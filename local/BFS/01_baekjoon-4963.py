from collections import deque
import sys
read = sys.stdin.readline
def BFS(x, y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    islandMap[x][y] = 0
    queue = deque()
    queue.append([x,y])
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and islandMap[nx][ny] == 1:
                islandMap[nx][ny] = 0
                queue.append([nx,ny])

while True:
    w, h = map(int, input().split())
    count = 0
    if w == 0 and h == 0:
        break
    islandMap = []
    for i in range(h):
        islandMap.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if islandMap[i][j] == 1 :
                BFS(i,j)
                count += 1
    print(count)
