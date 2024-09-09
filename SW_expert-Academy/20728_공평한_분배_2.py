T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    candy = list(map(int, input().split()))
    answer = 2147000000
    candy = sorted(candy)
    start = 0
    end = K - 1
    while (end <= N - 1):
        answer = min(candy[end] - candy[start], answer)
        end += 1
        start += 1
    
    print('#{} {}' .format(test_case, answer))