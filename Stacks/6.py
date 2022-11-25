# https://leetcode.com/problems/car-fleet/

def carFleet(target, position, speed):

    pos_speed_lst = [[p, s] for p, s in zip(position, speed)]

    stack = []

    for p, s in sorted(pos_speed_lst)[::-1]:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    
    return len(stack)


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
print(carFleet(10, [3], [3]))
print(carFleet(100, [0, 2, 4], [4, 2, 1]))
