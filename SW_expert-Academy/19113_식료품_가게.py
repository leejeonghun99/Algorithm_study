T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    visited = [False] * N * 2
    answer = []
    for i in range(2*N - 1):
        for j in range(i, 2 * N):
            if arr[i] == arr[j] * 0.75 and visited[i] == False and visited[j] == False:
                visited[i] = True
                visited[j] = True
                answer.append(arr[i])
                if len(answer) == N+1:
                    break
        if len(answer) == N+1:
            break 
        answer2 = str(" ".join(map(str,answer)))
    print('#{} {}' .format(test_case, answer2))