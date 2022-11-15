# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):

    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False


print(containsDuplicate([1, 2, 3, 1]))