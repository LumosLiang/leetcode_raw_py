class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2: return n
        
        a, b, c = 1, 2, 0
        
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        
        return c
            
