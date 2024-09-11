N, K = map(int,input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)
left = 0
right = N - 1
answer = 0
while left < right:
    if arr[left] + arr[right] > K :
        right -= 1
    else:
        left += 1
        right -= 1
        answer += 1
print(answer)