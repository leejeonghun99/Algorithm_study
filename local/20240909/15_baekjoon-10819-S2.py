N= int(input())

A = list(map(int,input().split()))
arr = []
answer = 0
visited = [False] * N

def back():
    global answer
    if len(arr) == N:
        answer = max(answer, cal(arr))
        return
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            arr.append(A[i])
            back()
            arr.pop()
            visited[i] = False

def cal(arr):
    sum = 0
    for i in range(N - 1):
        sum += abs(arr[i] - arr[i+1])
    return sum
back()
print(answer)
