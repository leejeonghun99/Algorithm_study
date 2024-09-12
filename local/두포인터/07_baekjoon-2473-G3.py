N = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

answer = float('inf') 
result = []  


for i in range(N - 2):
    start = i + 1
    end = N - 1
    while start < end:
        total = arr[i] + arr[start] + arr[end]
        if abs(total) < abs(answer):
            answer = total
            result = [arr[i], arr[start], arr[end]]
        if total == 0:
            break
        elif total > 0:
            end -= 1
        else:
            start += 1
print(' '.join(map(str, result)))