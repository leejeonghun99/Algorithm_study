S = list(input().strip())  
T = list(input().strip())  

def back(arr):
    if arr == S:
        print(1)
        exit()  
    if len(arr) <= len(S):
        return  
    if arr[-1] == 'A':
        back(arr[:-1])
    
    if arr[0] == 'B':
        back(arr[1:][::-1])

back(T)
print(0)  