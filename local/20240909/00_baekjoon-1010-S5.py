T = int(input())

def bridge(N):
    num = 1
    for i in range(1, N + 1):
        num *= i
    return num
            

for _ in range (T): 
    N, M = map(int, input().split())
    answer = bridge(M) / (bridge(N) * bridge(M - N))
    print(int(answer))