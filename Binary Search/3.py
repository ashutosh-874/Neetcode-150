# https://leetcode.com/problems/koko-eating-bananas/

import math

def minEatingSpeed(piles, h):

    res = max(piles)

    l, r = 1, res
    
    while l <= r:

        m = (l+r) // 2

        time = 0
        for pile in piles:
            time += math.ceil(pile / m)
        
        # print(time)
        
        if time > h:
            l = m + 1
        elif time <= h:
            res = min(m, res)
            r = m - 1

    return res
        




    
print(minEatingSpeed([3, 6, 7, 11], 8))
print(minEatingSpeed([30,11,23,4,20], 5))
print(minEatingSpeed([30,11,23,4,20], 6))