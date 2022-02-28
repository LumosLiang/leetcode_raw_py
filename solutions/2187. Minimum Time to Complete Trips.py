class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        ## binary search
        
        l, r = 1, time[-1] * totalTrips
        
        while l < r:
            mid = (l + r) // 2
            
            ts = sum([mid // t for t in time])
            
            if ts < totalTrips:
                l = mid + 1
            else:
                r = mid
        
        return l
                
            
        
            
            
                
            
            
        
