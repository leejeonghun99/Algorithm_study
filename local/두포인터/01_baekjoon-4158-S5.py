import sys
input = sys.stdin.readline
print = sys.stdout.write

res = []
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    sang = set([int(input()) for _ in range(n)])
    sun = set([int(input()) for _ in range(m)])
    res.append(str(len(sang&sun)))
    
print("\n".join(res))