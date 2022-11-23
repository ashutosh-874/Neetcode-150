# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque

def maxSlidingWindow(nums, k):
    
    res = []
    q = deque()

    l = 0

    for r in range(len(nums)):

        # pop smaller values from right of q 
        num = nums[r]
        while q and nums[q[-1]] < num:
            q.pop()
        q.append(r)

        # remove out of window els
        if l > q[0]:
            q.popleft()

        if (r+1) >= k:
            res.append(nums[q[0]])
            l += 1

    return res






print(maxSlidingWindow([3, -1, -3, 5, 3, 6, 7, 3], 3))
print(maxSlidingWindow([1], 1))


