class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0: return 0
        
        ispos = True if x > 0 else False
        
        res = 0
        x = abs(x)
        while x:
            temp = res * 10 + x % 10
            if temp > 2 ** 31 - 1 or  temp < - 2 ** 31 - 1 : return 0
            res = temp
            x = x // 10
            
        return res if ispos else res * -1
            
​
