def solution(numbers, target):
    answer = 0
    def dfs(depth, num):
        nonlocal answer
        if depth == len(numbers):
            if num == target:
                answer += 1
            return
        dfs(depth + 1, num + numbers[depth])
        dfs(depth + 1, num - numbers[depth])
    dfs(1, numbers[0])
    return answer

print(solution([1, 1, 1, 1, 1], 3))