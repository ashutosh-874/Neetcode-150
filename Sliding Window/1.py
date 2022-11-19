# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/



def maxProfit(prices):

    if len(prices) <= 1: return 0

    max_arr = [0 for i in range(len(prices))]

    cur_max = 0
    for idx in range(len(prices) - 1, -1, -1):
        max_arr[idx] = cur_max
        cur_max = max(cur_max, prices[idx])
    
    res = 0
    for idx in range(len(prices)):
        if max_arr[idx] > prices[idx]:
            res = max(res, max_arr[idx] - prices[idx])

    return res




print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([7, 1, 5, 3, 6, 4, 5]))


