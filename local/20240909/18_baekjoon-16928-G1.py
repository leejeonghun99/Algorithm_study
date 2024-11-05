from collections import deque

N, M = map(int, input().split())

board_map = [0] * 101

visited = [False] * 101

ladder = dict()
snake = dict()

for _ in range(N):
    a, b = map(int,input().split())
    ladder[a] = b
for _ in range(M):
    a, b = map(int,input().split())
    snake[a] = b

queue = deque()
queue.append(1)

while queue:
    num = queue.popleft()
    if num == 100:
        break
    for i in range(1,7):
        move = num + i
        if move <= 100 and visited[move] == False:
            if move in ladder.keys():
                move = ladder[move]
            elif move in snake.keys():
                move = snake[move]
            if visited[move] == False:
                visited[move] = True
                board_map[move] = board_map[num] + 1
                queue.append(move)

print(board_map[100])

