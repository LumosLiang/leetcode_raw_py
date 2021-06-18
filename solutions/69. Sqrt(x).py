class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        lo, hi = 0, x 
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid ** 2 == x: return mid
            elif mid ** 2 > x: hi = mid - 1
            else: lo = mid + 1 
            
        return hi
        
