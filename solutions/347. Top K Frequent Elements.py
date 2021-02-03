from collections import Counter
import heapq
​
class Solution:
    def topKFrequent(self, nums, k):
        res = []
        dict_nums = Counter(nums)
        
        maxheap = [(-val, key) for key, val in dict_nums.items()]
        heapq.heapify(maxheap)
​
        for _ in range(k):
            res.append(heapq.heappop(maxheap)[1])
        return res
