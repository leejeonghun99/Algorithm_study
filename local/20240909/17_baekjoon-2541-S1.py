N, d, k, c = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr = arr * 2
answer_arr = arr[:k]
answer = len(set(answer_arr))

if c not in answer_arr:
    answer += 1
for i in range(1, N):
    answer_arr.pop(0)
    answer_arr.append(arr[i + k - 1])
    if c not in answer_arr:
        answer = max(answer, len(set(answer_arr)) + 1)
    else:
        answer = max(answer, len(set(answer_arr)))
    if answer == d:
        break
print(answer)
    
