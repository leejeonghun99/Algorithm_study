T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    score = [0] * 101
    answer = 0
    arr = list(map(int, input().split()))
    for i in arr:
        score[i] += 1
        answer = max(answer, score[i] )
        if answer == score[i]:
            max_num = i
    print('#{} {}' .format(test_case, max_num))