class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0: return 1
        if n == 1: return x
        if n == -1: return 1/x
        
        base = 0
        
        if n % 2 == 0:
            base = self.myPow(x, n / 2) 
            return base * base
        else:
            base = self.myPow(x, (n - 1) / 2)
            return x * base * base
        
        
