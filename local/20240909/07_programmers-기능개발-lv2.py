def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            arr.append((100 - progresses[i]) // speeds[i])
        else :
            arr.append((100 - progresses[i]) // speeds[i] + 1)
    
    count = 1
    while True:
        if len(arr) > count and arr[0] >= arr[count]:
            count += 1
        elif len(arr) > count and arr[0] < arr[count]:
            answer.append(count)
            arr = arr[count:]
            count = 1
        else:
            answer.append(count)
            break
        
    return answer