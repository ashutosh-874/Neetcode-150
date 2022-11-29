# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


def findMin(nums):


    left, right = 0, len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        # left sorted portion
        if nums[mid] >= nums[left]:
            if nums[right] < nums[left]:
                left = mid + 1
            else:
                return nums[left]

        # right sorted portion
        else:
            right = mid

    
print(findMin([3, 4, 5, 1, 2]))
print(findMin([4, 5, 6, 7,0, 1, 2]))
print(findMin([11, 13, 15, 17]))
print(findMin([5, 0, 3]))
print(findMin([5,1,2,3,4]))