arr = [1,2,3,4]
visited = [0] * len(arr)

def permutations(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            #visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            #visited[i] = 0

permutations(2, [])

# 중복순열은 여기서 visited함수가 필요없다.