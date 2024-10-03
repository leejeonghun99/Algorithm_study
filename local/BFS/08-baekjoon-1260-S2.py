from collections import deque

N, M, V = map(int, input().split())

arr = [[False for _ in range(N) ] for _ in range(N)]

print(arr)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = True
    arr[b - 1][a - 1] = True

Bvisited = [False for _ in range(N)]
Dvisited = [False for _ in range(N)]
rrr = []

kkk = []

def DFS(v):
    Dvisited[v] = True
    rrr.append(v + 1)
    for i in range(N):
        if Dvisited[i] == False and arr[v][i] == True:
            DFS(i)


def BFS(v):
    queue = deque()
    Bvisited[v] = True
    queue.append(v)
    while queue:
        a = queue.popleft()
        kkk.append(a+1)
        for i in range(N):
            if Bvisited[i] == False and arr[a][i] == True:
                Bvisited[i] = True
                queue.append(i)



DFS(V - 1)
print(rrr)
BFS(V - 1)
print(kkk)