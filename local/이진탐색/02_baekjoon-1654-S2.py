import sys
K, N = map(int, input().split())

length = []

for _ in range(K):
    length.append(int(input()))


start = 1
end = max(length)
mid = (start + end) // 2

num = 0

while start <= end:
    num = 0
    for i in range(K):
        num += length[i] // mid
    if num >= N:
        start = mid + 1
        mid = (start + end) // 2
    elif num < N :
        end = mid - 1
        mid = (start + end) // 2

print(end)
