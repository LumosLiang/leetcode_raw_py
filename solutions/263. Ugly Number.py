class Solution:
    def isUgly(self, n: int) -> bool:
        
        if not n: return False
        
        while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            if not n % 2: 
                n //= 2
                continue
                
            elif not n % 3: 
                n //= 3
                continue
    
            else:
                n //= 5;
            
        return n == 1
    
