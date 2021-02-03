from collections import Counter
import heapq
​
class Solution:
    def topKFrequent(self, words, k):
        
        dict_w = Counter(words)
        maxheap = [(-v, k) for k,v in dict_w.items()]
        res = []
        heapq.heapify(maxheap)
        for _ in range(k):
            res.append(heapq.heappop(maxheap)[1])
        
        return res
