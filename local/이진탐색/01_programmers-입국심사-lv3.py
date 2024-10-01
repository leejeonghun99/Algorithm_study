def solution(n, times):
    answer = 0
    times.sort()
    start, end = 1, times[-1] * n

    while start <= end:
        center = (start + end) // 2
        num = 0
        for i in times:
            num += center // i
            if num >= n:
                break
        if num >= n:
            answer = center
            end = center -  1
        else:
            start = center + 1
        
    return answer