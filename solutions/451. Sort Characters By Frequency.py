class Solution:
    def frequencySort(self, s: str) -> str:
        return self.sol2(s)
    def sol1(self, s):
        fre = collections.Counter(s)
        fre = [[-v, k] for k, v in fre.items()]
        fre.sort()
        
        res = ""
        
        for f in fre:
            res += f[1] * -f[0]
        
        return res
    
    def sol2(self, s):
        
        dic = collections.Counter(s)
        
        heap = []
        for k, v in dic.items():
            heapq.heappush(heap, (-v, k))
            
        res = ''
        for _ in range(len(heap)):
            v, k = heapq.heappop(heap)
            res += k * -v
            
        return res
