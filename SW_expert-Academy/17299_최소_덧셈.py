T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = input()
    S = len(N)
    if S % 2 == 0:
        a = int(''.join(N[:S//2]))
        b = int(''.join(N[S//2:]))
        print('#{} {}'.format(test_case, a+b))
    else:
        a = int(''.join(N[:S//2]))
        b = int(''.join(N[S//2:]))
        c = int(''.join(N[:S//2+1]))
        d = int(''.join(N[S//2 + 1:]))
        print('#{} {}'.format(test_case, min(a+b, c+d)))