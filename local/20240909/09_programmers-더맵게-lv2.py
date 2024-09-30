def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True:
        num = scoville[0] + scoville[1] * 2
        scoville.remove(scoville[0])
        scoville.remove(scoville[1])
        scoville.append(num)
        scoville.sort()
        answer += 1
        if scoville[0] >= K:
            break
        if len(scoville) < 2:
            answer = -1
            break
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))