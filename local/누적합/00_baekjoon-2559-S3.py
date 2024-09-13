N, K = map(int, input().split())

arr = list(map(int, input().split()))
num = 0
answer = float('-inf')
for i in range(N):
    num += arr[i]
    arr[i] = num

for i in range(K - 1, N):
    if i == K - 1:
        answer = max(answer, arr[i])
    else:
        answer = max(answer, arr[i] - arr[i - K])
print(answer)