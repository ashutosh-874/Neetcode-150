
# https://leetcode.com/problems/daily-temperatures/


def dailyTemperatures(temperatures):
    stack = []
        
    for idx in range(len(temperatures)-1, -1, -1):
        

        while stack and stack[-1][0] <= temperatures[idx]:
            stack.pop()

        to_append =  (temperatures[idx], idx)

        if not stack:
            temperatures[idx] = 0
        else:
            temperatures[idx] = stack[-1][1] - idx

        stack.append(to_append)
        
        # print(temperatures, stack)
     
    return temperatures


print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60, 90]))
print(dailyTemperatures([30]))
print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))