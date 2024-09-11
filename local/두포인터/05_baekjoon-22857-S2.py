def solution(numbers):
    answer = []
    length = len(numbers)
    stack = []
    answer = [-1] * length
    for i in range(length):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer

arr = list(map(int, input().split()))
print(solution(arr))