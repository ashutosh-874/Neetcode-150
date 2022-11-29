# https://leetcode.com/problems/search-in-rotated-sorted-array/


def search(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:
        
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        # left sorted portion
        if nums[mid] >= nums[left]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1







print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,8,1,2,3], 8))
print(search([4,5,6,7,0,1,2],2))
print(search([1],1))
print(search([5, 1, 3],3))
print(search([5, 1, 3],0))
print(search([3, 1],1))

