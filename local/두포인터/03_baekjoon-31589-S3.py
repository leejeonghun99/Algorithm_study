N, K = map(int, input().split())

arr = list(map(int, input().split()))

arr = sorted(arr)
left = 0
right = N - 1
answer = 0
al = []
for i in range(1,K + 1):
    if(i % 2 == 1):
        al.append(arr[right])
        right -= 1
    else:
        al.append(arr[left])
        left += 1

for i in range(len(al)):
    if(i>1 and i % 2 == 0):
        answer += al[i] - al[i - 1]
    if(i == 0):
        answer += al[0]
print(answer)