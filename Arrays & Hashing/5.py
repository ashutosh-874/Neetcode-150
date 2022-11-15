# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
from heapq import heappush, heappop

def topKFrequent(nums, k):
    
    dct = Counter(nums)
    max_heap = []

    for key, val in dct.items():
        heappush(max_heap, (-val, key))

    res = []
    for _ in range(k):
        res.append(heappop(max_heap)[1])

    return res

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
