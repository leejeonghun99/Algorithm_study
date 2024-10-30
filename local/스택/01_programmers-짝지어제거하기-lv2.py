from collections import deque
def solution(s):
    answer = 1
    
    queue = deque()
    queue.append(0)
    for i in s:
        if queue[-1] == i:
            queue.pop()
        else:
            queue.append(i)
    if len(queue) > 1:
        answer = 0
    return answer