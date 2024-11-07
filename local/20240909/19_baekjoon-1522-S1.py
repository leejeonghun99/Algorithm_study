aorb = input()
CountA = aorb.count('a')

answer = 1000
aorb1 = aorb * 2
for i in range(len(aorb)):
    answer = min(answer, aorb1[i:i+CountA].count('b'))
    if answer == 0:
        break
print(answer)