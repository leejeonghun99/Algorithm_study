numbers = list(range(1, 10_001))
visited = []
for i in numbers:
    for n in str(i):
        i += int(n)
    if i <= 10_000:
        visited.append(i)

for i in set(visited):
    numbers.remove(i)
for i in numbers:
    print(i)