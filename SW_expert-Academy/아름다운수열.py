N = int(input())
arr = []
arr2 = []
for i in range(N):
    arr.append(int(input()))

M = int(input())

for i in range(M):
    arr2.append(int(input()))

length = len(arr2)
arr4 = []
arr6 = sorted(arr2)

def is_increasing_by(arr1, arr2, increment):
    # 두 배열의 길이가 다르면 False 반환
    if len(arr1) != len(arr2):
        return False
    
    # 각 요소의 차이가 increment와 같은지 확인
    for i in range(len(arr1)):
        if arr2[i] - arr1[i] != increment:
            return False
    
    return True


for i in range(N-M+1):
    arr3 = []
    arr5 = []
    for j in range(i,M+i):
        arr3.append(arr[j])
    arr5 = sorted(arr3)
    if arr5 == arr6:
        arr4.append(i+1)
    elif is_increasing_by(arr3, arr2, arr2[0] - arr3[0]):
        arr4.append(i+1)
    elif is_increasing_by(arr5, arr6, arr6[0] - arr5[0]):
        arr4.append(i+1)
print(len(arr4))
for i in range(len(arr4)):
    print(arr4[i])
