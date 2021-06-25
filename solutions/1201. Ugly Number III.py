class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lo, hi = min(a,b,c), min(a,b,c) * n
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            ab = (a * b) // math.gcd(a, b)
            bc = (c * b) // math.gcd(c, b)
            ac = (a * c) // math.gcd(a, c)
            abc = (a * bc) // math.gcd(a, bc)
            
            count = mid // a + mid // b + mid // c - (mid // ab + mid // bc + mid // ac) + mid // abc
            
            if count >= n: hi = mid
            else: lo = mid + 1
            
        return lo
