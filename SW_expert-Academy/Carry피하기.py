def is_valid_combination(combination):
    sums = [0] * 10
    for num in combination:
        str_num = str(num)
        for i, digit in enumerate(reversed(str_num)):
            sums[i] += int(digit)
            if sums[i] >= 10:
                return False
    return True

def backtrack(nums, index, current_combination):
    global max_count

    if index == len(nums):
        if is_valid_combination(current_combination):
            max_count = max(max_count, len(current_combination))
        return

    # Include the current number
    current_combination.append(nums[index])
    if is_valid_combination(current_combination):
        backtrack(nums, index + 1, current_combination)
    current_combination.pop()

    # Exclude the current number
    backtrack(nums, index + 1, current_combination)

def max_no_carry_numbers(nums):
    global max_count
    max_count = 0
    backtrack(nums, 0, [])
    return max_count

# 입력 처리
n = int(input())
nums = [int(input()) for _ in range(n)]

# 함수 호출 및 결과 출력
print(max_no_carry_numbers(nums))
