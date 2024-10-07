import math
T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    length = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 )

    if length == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1 + r2 == length or abs(r1 - r2) == length:
            print(1)
        elif (abs(r1 - r2) < length) and (r1 + r2 > length):
            print(2)
        else:
            print(0)