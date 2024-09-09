from collections import deque
# 1. 반복 횟수와 추가되는 번호의 갯수 입력
K, M = map(int, input())

# 2. 맵 입력 받기
thrasher = []

for _ in range(5):
    thrasher.append(list(map(int, input().split())))

dy = [1, 0 , -1, 0]
dx = [0, 1, 0 -1]

isExit = [[False] * 5 for _ in range(5)]



# 3. 추가 번호 배열 입력
bonus = deque()
bonus.append(list(map(int, input().split())))

def inRange(y,x):
    return 0 <= y < 5 and 0 <=x < 5

# 4. 보너스 맵 추가 함수
def fill() :
    for i in range(5):
        for j in range(5, -1, -1):
            if isExit[j][i] == True:
                a = bonus.popleft()
                thrasher[j][i] = a
                isExit[j][i] = True

count = 0

# 점수 계산
def BFS(y,x) :
    num = thrasher[y][x]
    queue = deque()
    queue.append((y,x))
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if inRange(ny, nx) and thrasher[ny][nx] == num and isExit[ny][nx] == False:
                isExit[ny][nx] = True
                global count
                count += 1
                BFS(ny,nx)
                
def turn
