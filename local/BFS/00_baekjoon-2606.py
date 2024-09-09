from collections import deque
computer = int(input())
cnt = int(input())
comMap = [[] for _ in range(computer + 1)] 

for _ in range(cnt):
    A, B = map(int, input().split())
    comMap[A].append(B)
    comMap[B].append(A)
visited = [False] * (computer + 1)
answer = 0
visited[1]=True
Q=deque([1])
while Q:
    c=Q.popleft()
    for nx in comMap[c]:
        if visited[nx]==False:
            Q.append(nx)
            visited[nx]=True
            answer += 1
print(answer)