num = int(input())

num2 = int(num / 3)
count = 0
for i in range(0, num2 + 1):
    if (num - i * 3) % 5 == 0:
        count = i + int((num - i * 3) / 5)
        break
if count == 0:
    count = -1
if num == 3:
    count = 1
print(count)
