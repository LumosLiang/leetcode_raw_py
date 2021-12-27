class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        lo, hi = 1, num
        
        while lo < hi:
            mid = (lo + hi) // 2
            target = mid ** 2
            
            if target < num:
                lo = mid + 1
            else:
                hi = mid
     
        return True if lo ** 2 == num else False
