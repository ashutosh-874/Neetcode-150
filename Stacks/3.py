# https://leetcode.com/problems/evaluate-reverse-polish-notation/


def evalRPN(tokens):
    
    ops = ["+", '-', '*', '/']

    stack = []

    for token in tokens:
        if token in ops:
            y = stack.pop()
            x = stack.pop()
            if token == '/':
                stack.append(str(eval(x + token + token + y)))
            else:
                stack.append(str(eval(x + token + y)))
        else:
            stack.append(token)

    return stack.pop()


print(evalRPN(["2","1","+","3","*"]))