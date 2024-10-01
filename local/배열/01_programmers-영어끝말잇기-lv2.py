def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            answer = []
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
        word = words[:i + 1]
        if word.count(words[i]) > 1:
            answer = []
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
        if len(words[i]) == 1:
            answer = []
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
    return answer