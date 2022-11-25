# https://leetcode.com/problems/largest-rectangle-in-histogram/


def largestRectangleArea(heights):


    stack = []
    res = -float('inf')
    l = len(heights)

    for idx, height in enumerate(heights):

        # remove els from stack whose height is > than current height & cal their areas
        popped = None
        while stack and stack[-1][1] > height:
            popped = stack.pop()
            res = max(res, (idx - popped[0])*popped[1] )
        if popped:
            stack.append((popped[0], height))
        else:
            stack.append((idx, height))

    # remove els form elements whose area covers till the end
    while stack:
        popped = stack.pop()
        res = max(res, (l - popped[0])*popped[1])

    return res








print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
