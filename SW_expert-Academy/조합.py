arr = [1,2,3,4]

def combination(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combination(n, new_arr + [arr[i]], i + 1 )

combination(2, [], 0)