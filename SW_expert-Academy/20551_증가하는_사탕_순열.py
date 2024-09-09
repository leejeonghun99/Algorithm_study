T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    x, y, z = map(int, input().split())
    answer = 0

    if z < 3 or y < 2 or x < 1:
        answer = -1
    else :
        if y > z - 1:
            answer = answer + y - z + 1
        if x > z - 2:
            answer = answer + x - z + 2
    print('#{} {}'.format(test_case, answer))