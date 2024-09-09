a = 100
result = 0
for i in range(1,3):
    print(result)
    result = a >> i
    print(result)
    result = result + 1
print(result)