import collections 
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        
        dic = collections.Counter(s)
            
        heap = []
        for k, v in dic.items():
            heapq.heappush(heap, (v, k))
            
        res = ''
        for _ in range(len(heap)):
            v, k = heapq.heappop(heap)
            res = k * v + res
        
        return res
