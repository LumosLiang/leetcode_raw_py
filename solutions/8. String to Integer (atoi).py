class Solution:
    def myAtoi(self, s: str) -> int:
        
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        
        if i >= len(s): return 0
        
        sign = 1
        if s[i] in ["-","+"]:
            if s[i] == "-": 
                sign = -1
            i += 1
            
        if i >= len(s): return 0
        
        res = 0
        while i < len(s) and ord("0") <= ord(s[i]) <= ord("9"):
            res = res * 10  + (ord(s[i]) - ord("0"))
            i += 1
        
        return min(max(res * sign, -2 ** 31), 2**31 - 1)
    
  
    
        
    
            
