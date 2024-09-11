N, M = map(int,input().split())

A = list(map(int, input().split()))

answer = 0
pointOne = 0
pointTwo = 1
sumnum = A[0]
while True:
    if sumnum < M:
        if pointTwo < N:
            sumnum += A[pointTwo]
            pointTwo += 1
        else:
            break
    elif sumnum == M:
        answer += 1
        sumnum -= A[pointOne]
        pointOne += 1
    else :
        sumnum -= A[pointOne]
        pointOne += 1
print(answer)

