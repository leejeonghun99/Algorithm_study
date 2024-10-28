def solution(s, n):
    answer = []  # answer를 리스트로 초기화하여 append 사용 가능하게 변경
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 문자열로 정의
    small = "abcdefghijklmnopqrstuvwxyz"  # 문자열로 정의

    for char in s:
        if char in big:
            new_char = big[(big.index(char) + n) % len(big)]  # 리스트 대신 index() 사용
            answer.append(new_char)
        elif char in small:
            new_char = small[(small.index(char) + n) % len(small)]
            answer.append(new_char)
        else:
            answer.append(char)  # 공백이나 특수문자 그대로 추가

    return ''.join(answer)  # 리스트 answer를 문자열로 변환하여 반환