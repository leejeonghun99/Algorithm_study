def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        num = commands[i][2] - 1
        arr = array[start:end]
        arr = sorted(arr)
        answer.append(arr[num])
    return answer