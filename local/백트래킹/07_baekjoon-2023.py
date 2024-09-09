N = int(input())

answer = []

def back(x):
    if len(str(x)) == N:
        print(x)
    else :
        for i in range(1,10):
            if i % 2 == 0:
                continue
            if prime(x * 10 + i):
                back(x * 10 + i)

def prime(x):
    for i in range(2, int(x / 2 + 1)):
        if x % i == 0:
            return False
    return True

back(2)
back(3)
back(5)
back(7)