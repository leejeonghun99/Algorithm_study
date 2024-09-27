from collections import deque

def solution(maps):
    answer = -1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    depths = []
    def bfs(x, y):
        nonlocal dx, dy, answer, depths
        depth = 1
        queue = deque()
        queue.append([x, y, depth])
        while queue:
            a, b, d = queue.popleft()
            if a == len(maps) - 1 and b == len(maps[0]) - 1:
                answer = d
                break
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if maps[nx][ny] == 1:
                        maps[nx][ny] = 0
                        queue.append([nx, ny, d + 1])
        
    bfs(0, 0)
    return answer