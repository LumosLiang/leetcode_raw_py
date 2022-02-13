class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        
        beans.sort()
        
        l, s, res = len(beans), sum(beans), float('inf')
        
        for i in range(l):
            
            res = min(res, s - (l - i) * beans[i])
            
        return res
            
        
