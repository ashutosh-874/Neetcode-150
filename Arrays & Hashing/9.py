# https://leetcode.com/problems/longest-consecutive-sequence/

    



def longestConsecutive(nums):
    if len(nums) < 1:
        return 0

    
    s = set(nums)

    def is_start_of_sequence(n):
        return n-1 not in s

    res = -float('inf')
    for num in nums:
        if is_start_of_sequence(num):
            c = 1
            while num + 1 in s:
                num += 1
                c += 1
            res = max(res, c)

    return res





print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
