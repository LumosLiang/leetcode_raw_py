class Solution:
    def romanToInt(self, s: str) -> int:
         
        return self.sol2(s)
    # with exception
    def sol1(self, s):    
        hash = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L': 50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
​
        
        res, p = 0, 0
        
        while p < len(s) - 1:
            k = s[p:p + 2] 
            if k in hash:
                res += hash[k]
                p += 2
            else:
                res += hash[s[p]]
                p += 1
            
        return res if p == len(s) else (res + hash[s[p]])
        
        
    # with out exception
    def sol2(self, s):
        
        hash = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
    
#         MCMXCIV
                
#         1000 + (-100) + 1000 + (-10) + 100 + (-1) + 5 = 
                
        res, p = 0, 0
                
        while p < len(s) - 1:
            curr, nxt = hash[s[p]], hash[s[p + 1]]
            if curr >= nxt:
                res += curr
            else:
                res -= curr
            p += 1
        
        return res + hash[s[p]]
            
        
