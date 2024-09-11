N = int(input())
arr = []
for _ in range(N):
    weight, hight = map(int, input().split())
    arr.append([weight, hight])
answer = []
for i in arr:
    score = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            score += 1
    answer.append(score)

print(' '.join(map(str,answer)))