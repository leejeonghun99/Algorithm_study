N, M = map(int,input().split())
arr = list(map(int, input().split()))
answer = 0
left, right = 0, N - 1
arr = sorted(arr)
while left < right:
    if arr[left] + arr[right] < M:
        left += 1
    elif arr[left] + arr[right] >= M :
        right -= 1
        left += 1
        answer += 1

print(answer)