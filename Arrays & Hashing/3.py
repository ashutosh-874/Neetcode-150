# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):

    dct = {}

    for idx, num in enumerate(nums):
        if (target - num) in dct:
            return [idx, dct[target - num]]
        else:
            dct[num] = idx


print(twoSum([3, 3], 6))  
        