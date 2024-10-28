def solution(want, number, discount):
    answer = 0
    isTrue = False
    for i in range(len(discount) - 9):
        isTrue = False
        for j in range(len(want)):
            if discount[i:i+10].count(want[j]) != number[j]:
                isTrue = True
                break
        if isTrue == False:
            answer += 1
    return answer