N = int(input())
K = int(input())
Sensor = list(map(int, input().split()))

Sensor.sort()

arr = []

for i in range(N - 1):
    arr.append(Sensor[i+1] - Sensor[i])
arr.sort()
print(sum(arr[:N - K]))
