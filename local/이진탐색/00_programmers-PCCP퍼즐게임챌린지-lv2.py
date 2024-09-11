def solution(diffs, times, limit):
    answer = 0
    left = 1
    right = max(diffs)
    while left < right:
        center = (left + right) // 2
        centerPoint = 0
        for i in range(len(diffs)):
            if i == 0:
                time_prev = 0
            else:
                time_prev = times[i-1]
            time_cur = times[i]
            if center >= diffs[i]:
                centerPoint += time_cur
            else:
                centerPoint += (diffs[i] - center) * (time_prev + time_cur) + time_cur
        if centerPoint <= limit:
            right = center
        else:
            left = center + 1
    answer = left
    return answer