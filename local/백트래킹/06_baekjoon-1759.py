L, C = map(int, input().split())
arr = list(input().split())

moeum = ['a', 'e', 'i', 'o', 'u']

arr = sorted(arr)

def back(start, answer, count_vowel, count_consonant):
    if len(answer) == L:
        if count_vowel >= 1 and count_consonant >= 2:
            print(''.join(answer))
        return

    for i in range(start, C):
        if arr[i] in moeum:
            back(i + 1, answer + [arr[i]], count_vowel + 1, count_consonant)
        else:
            back(i + 1, answer + [arr[i]], count_vowel, count_consonant + 1)

back(0, [], 0, 0)
