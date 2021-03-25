class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        end = piles[-1]
        start = 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            temp = 0
            for p in piles:
                if not p % mid: temp += p // mid
                else: temp += p // mid + 1
            
            if temp <= h: 
                end = mid - 1
            else:
                start = mid + 1
                
        return start
            
​
            
        
        
