# https://leetcode.com/problems/valid-parentheses/


def isValid(s):

    stack = []

    open_brackets = ['(', '{', '[']
    closing_brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for i in s:
        if i in open_brackets:
            stack.append(i)
        else:
            if not stack or not closing_brackets[i] == stack.pop():
                return False
    
    return True if len(stack) == 0 else False


print(isValid('[(())]{}]'))
