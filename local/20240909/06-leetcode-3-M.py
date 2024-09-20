from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        num = 0
        max_count = 0
        queue = deque()
        for i in range(len(s)):
            for j in queue:
                lll = s.count(j,num,i + 1)
                if lll > 1:
                    queue.popleft()
                    num += 1
                    count -= 1
                    break
            count += 1
            queue.append(s[i])
            max_count = max(count, max_count)
        return max_count
    print(lengthOfLongestSubstring(0," "))

## 비교 배열안에는 같은 알파벳이 없어야 한다.