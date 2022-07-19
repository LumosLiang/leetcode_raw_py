class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        pre, l = 0, len(s)
        prefix = [0] * l
        
        for post in range(1, l):
            
            while pre > 0 and s[pre] != s[post]:
                
                pre = prefix[pre - 1]
            if s[pre] == s[post]:
                pre += 1
            prefix[post] = pre
        
        print(prefix)
        if prefix[l - 1] != 0 and not l % (l - prefix[l - 1]):
            return True
        return False
    
    
    
    
