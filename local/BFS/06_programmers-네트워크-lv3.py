from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(num):
        nonlocal answer, visited
        queue = deque()
        queue.append(num)
        while queue:
            a = queue.popleft()
            for i in range(n):
                if computers[num][i] == 1 and visited[i] == False:
                    visited[i] = True
                    bfs(i)
                    queue.append(i)
                    
    
    for i in range(n):
        if visited[i] == False:
            bfs(i)
            answer += 1
    return answer