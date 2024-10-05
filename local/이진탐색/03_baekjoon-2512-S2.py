N = int(input())

cash = list(map(int, input().split()))

maximum = int(input())

start = 1
end = max(cash)
sumcash = 0
while start <= end:
    mid = (start + end) // 2
    sumcash = 0
    for i in cash:
        if i > mid:
            sumcash += mid
        else:
            sumcash += i
    if sumcash > maximum:
        end = mid - 1
    else :
        start = mid + 1
print(end)

    