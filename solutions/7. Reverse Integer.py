class Solution:
    def reverse(self, x: int) -> int:
        
        ans = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        if x == 2 ** 31: return 0
        
        MAX = 2 ** 31 - 1
        
        while x:
            r = x % 10
            
            if ans <= MAX // 10 and ans * 10 <= MAX - r:
                
                ans = ans * 10 + r
                # if (temp - r) // 10 != ans: return 0
​
                x = x // 10
            else: return 0
            
        return ans * sign
    
    # 1, negative
    # 2, overflow
