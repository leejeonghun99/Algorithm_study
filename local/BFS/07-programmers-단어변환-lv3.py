from collections import deque

def solution(begin, target, words):

    answer = 0

    if target not in words:
        return answer
    queue = deque()
    queue.append((begin,answer))
    while queue:
        visited = [0]*len(words)
        word,answer = queue.popleft()
        if word == target:
            break
        for i in range(len(words)):
            for j in range(len(words[i])):
                if word[j] == words[i][j]:
                    visited[i] +=1
        for i in range(len(visited)):
            if visited[i] == (len(target)-1):
                queue.append((words[i],answer+1))
                words[i] = str(answer)
    return answer
