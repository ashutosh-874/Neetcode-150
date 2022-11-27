# https://leetcode.com/problems/search-a-2d-matrix/

def b_search(nums, target):

    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l+r) // 2
        if nums[m] == target:
            return True
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1

    return False


def searchMatrix(matrix, target):

    lst = [x[-1] for x in matrix]

    l , r = 0, len(lst) - 1

    while l < r:
        m = (l+r) // 2
        if lst[m] == target:
            return True
        elif lst[m] > target:
            r = m
        else:
            l = m + 1

    return b_search(matrix[l], target)






print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 10))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60))
print(searchMatrix([[1],[10,11,16,20],[23,30,34,60]], 60))