# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


def twoSum(numbers, target):

    left, right = 0, len(numbers) - 1

    while numbers[left] + numbers[right] != target:
        if numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1

    return [left+1, right+1]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
print(twoSum([-1, 0], -1))



