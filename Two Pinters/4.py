# https://leetcode.com/problems/container-with-most-water/


def maxArea(height):

    res = -float('inf')


    l, r = 0, len(height) - 1

    while l < r:
        res = max(res, min(height[l], height[r]) * (r-l))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

    return res



print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))