# https://leetcode.com/problems/product-of-array-except-self/


def productExceptSelf(nums):

    res = [1] * len(nums)

    prod = nums[0]
    for idx in range(1, len(nums)):
        res[idx] = prod
        prod *= nums[idx]
    
    print(res)

    prod = 1
    for idx in range(len(nums) - 1, -1, -1):
        res[idx] *= prod
        prod *= nums[idx]

    return res




print(productExceptSelf([1, 2, 3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
        

