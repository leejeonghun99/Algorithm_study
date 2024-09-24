def solution(s):
    answer = []
    delTime = 0
    count = 0
    if s != "1":
        while len(s) > 1:
            count += 1
            delTime += len(s) - s.count("1")
            ordnum = str(bin(len(s) - s.count("1")))
            s = str(bin(s.count("1")))
            s = s.replace("0b", '')
            print(s)
        
    answer.append(count)
    answer.append(delTime)
    return answer