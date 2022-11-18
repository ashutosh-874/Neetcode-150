# https://leetcode.com/problems/3sum/

def twoSum(nums, target):

    left, right = 0, len(nums) - 1

    res = []

    while left < right:

        sm = nums[left] + nums[right]
        if sm > target:
            right -= 1
        elif sm < target:
            left += 1
        else:
            res.append([nums[left], nums[right]])
            left += 1
            while nums[left] == nums[left-1] and left < right:
                left += 1
            
    return res


def threeSum(nums):

    nums.sort()

    res = []

    for idx, num in enumerate(nums):

        if idx > 0 and nums[idx - 1] == num: continue

        for twoSumResult in twoSum(nums[idx+1:], 0-num):
            res.append([num] + twoSumResult)
    
    return res



print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 0, 0]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0,0]))