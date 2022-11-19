# https://leetcode.com/problems/trapping-rain-water/

def trap(height):
    length = len(height)
    if length <= 2: return 0

    # O(n) Memory + O(n) Time
    # max_left = [0 for i in range(length)]
    # max_right = [0 for i in range(length)]
    
    # max_l, max_r = 0, 0

    # for idx in range(length):
    #     max_left[idx] = max_l
    #     max_l = max(max_l, height[idx])
    # for idx in range(length-1, -1, -1):
    #     max_right[idx] = max_r
    #     max_r = max(max_r, height[idx])
    
    # res = 0
    # for idx in range(length):
    #     x = min(max_left[idx], max_right[idx]) - height[idx]
    #     if x > 0:
    #         res += x
    
    # return res

    # O(1) Memory + O(n) Time
    l, r = 0, length - 1
    max_left, max_right = height[l], height[r]
    
    res = 0
    while l < r:
        
        if max_left <= max_right:
            l += 1
            max_left = max(max_left, height[l])
            res += max_left - height[l]

        else:
            r -= 1
            max_right = max(max_right, height[r])
            res += max_right - height[r]
            
    return res


print(trap([4, 2, 0, 3, 2, 5]))
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4, 2, 3]))
print(trap([4, 2, 0]))
        

