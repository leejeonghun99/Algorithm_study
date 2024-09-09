from collections import deque

R, C, K = 0, 0, 0

MAX_L = 70

forest = [[0] * MAX_L for _ in range(MAX_L + 3)]
isExit = [[False] * MAX_L for _ in range(MAX_L + 3)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0

def isRange(y,x):
    return 3 <= y < R + 3 and 0 <= x < C

def resetMap():
    for i in range(R + 3):
        for j in range(C):
            forest[i][j] = 0
            isExit[i][j] = False

def canGo(y,x):
    flag = 0<= x - 1 and x + 1 < C and y + 1 < R + 3
    flag = flag and (forest[y - 1][x - 1] == 0)
    flag = flag and (forest[y - 1][x] == 0)
    flag = flag and (forest[y - 1][x + 1] == 0)
    flag = flag and (forest[y][x - 1] == 0)
    flag = flag and (forest[y][x] == 0)
    flag = flag and (forest[y][x + 1] == 0)
    flag = flag and (forest[y + 1][x] == 0)
    return flag

def BFS(y,x):
    queue = deque([(y,x)])
    result = y
    visit = [[False] * C for _ in range(R + 3)]
    visit[y][x] = True
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if isRange(ny, nx) and not visit[ny][nx] and (forest[ny][nx] == forest[cur_y][cur_y] or(forest[ny][nx] != 0 and isExit[cur_y][cur_x])):
                queue.append((ny,nx))
                visit[ny][nx] = True
                result = max(result, ny)
    return result

def down(y, x, d, id):
    if canGo(y+1, x):
        down(y+1, x, d, id)
    elif canGo(y+1, x - 1):
        down(y+1, x- 1, (d+3) % 4, id)
    elif canGo(y+1, x+1):
        down(y+1, x+1, (d+1)%4, id)
    else :
        if not isRange(y-1, x-1) or not isRange(y+1, x+1):
            resetMap()
        else :
            forest[y][x] = id
            for i in range(4):
                forest[y + dy[i]][x + dx[i]] = id
            isExit[y + dy[d]][x+dx[d]] = True
            global answer
            answer += BFS(y, x) - 3 + 1
def main():
    global R, C, K
    R, C, K = map(int, input().split())
    for id in range(1, K + 1): # 골렘 번호 id
        x, d = map(int, input().split()) # 골렘의 출발 x좌표, 방향 d를 입력받습니다
        down(0, x - 1, d, id)
    print(answer)

if __name__ == "__main__":
    main()