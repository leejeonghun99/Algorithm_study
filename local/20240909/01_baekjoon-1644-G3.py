N = int(input())

a = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False
if primes:
    answer = 0
    pointOne = 0
    pointTwo = 1
    sumnum = primes[0]
    while True:
        if sumnum < N:
            if pointTwo < len(primes):
                sumnum += primes[pointTwo]
                pointTwo += 1
            else:
                break
        elif sumnum == N:
            answer += 1
            sumnum -= primes[pointOne]
            pointOne += 1
        else :
            sumnum -= primes[pointOne]
            pointOne += 1
else:
    answer = 0
print(answer)
