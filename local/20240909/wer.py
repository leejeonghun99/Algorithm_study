def solution(name):
    answer = 0
    arr = list(name)
    count = ord(name[0]) - ord('A')
    answer = count
    arr.remove(name[0])
    for i in arr:
        if abs(count - ord(i)) > 13:
            answer += 26 - abs(count - ord(i)) 
            count = ord(i) - ord('A')
        else:
            answer += abs(count - ord(i))
            count = ord(i) - ord('A')
    return answer

print(solution("JAN"))