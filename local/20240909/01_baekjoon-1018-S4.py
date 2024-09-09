N, M = map(int, input().split())
arr = []
least = 64
for _ in range(N):  
    arr.append(list(input()))

def color(x, y):
    count1 = 0  
    count2 = 0 
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if (i + j) % 2 == 0:  
                if arr[i][j] != 'W':
                    count1 += 1
                if arr[i][j] != 'B':
                    count2 += 1
            else: 
                if arr[i][j] != 'B':
                    count1 += 1
                if arr[i][j] != 'W':
                    count2 += 1
    return min(count1, count2)

for i in range(N - 7):
    for j in range(M - 7):
        least = min(least, color(i, j))
        
print(least)