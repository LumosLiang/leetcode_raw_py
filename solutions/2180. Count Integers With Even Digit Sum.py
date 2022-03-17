class Solution:
    def countEven(self, num: int) -> int:
        
        # count digit
        
        res = 0
        
        for n in range(1, num + 1):
            if not self.digitcnt(n) % 2:
                res += 1
        return res
    
    def digitcnt(self, num):
        
        
        res = 0
        
        while num:
            res += num % 10
            num = num // 10
        
        return res
