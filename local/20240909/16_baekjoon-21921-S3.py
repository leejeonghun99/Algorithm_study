N, X = map(int, input().split())

arr = list(map(int, input().split()))

answer = sum(arr[:X])
counter = 1
num = answer

for i in range(1, N - X + 1):
    num = num - arr[i - 1] + arr[i + X - 1]
    if num > answer:
        counter = 1
        answer = num
    elif num == answer:
        counter += 1

if answer > 0:
    print(answer)
    print(counter)
else:
    print("SAD")


