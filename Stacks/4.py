# https://leetcode.com/problems/generate-parentheses/


def generateParenthesis(n):

    res = []

    def rec(string, o, c):

        if o == c == n:
            res.append(string)
            return

        if o > c:
            if o == n:
                rec(string + ')'*(o-c) , n, n)
            else:
                rec(string + '(', o+1, c)
                rec(string + ')', o, c+1)
        
        elif o == c:
            rec(string + '(', o+1, c)

        return

    rec('(', 1, 0)
    return res

print(generateParenthesis(5))


