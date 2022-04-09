class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.sol2(s)
    def sol1(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            
            # out of scope
            if not (48 <= ord(s[l]) <= 57 or 65 <= ord(s[l]) <= 90 or 97 <= ord(s[l]) <= 122):
                l += 1
                
            elif not (48 <= ord(s[r]) <= 57 or 65 <= ord(s[r]) <= 90 or 97 <= ord(s[r]) <= 122):
                r -= 1
                
            # in the scope
            else:
                lv = ord(s[l])
                rv = ord(s[r])
                if lv > 96: lv -= 32
                if rv > 96: rv -= 32
​
                if lv != rv:
                    return False
                l += 1
                r -= 1
            
        return True
    
    def sol2(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            lv, rv = s[l], s[r]
            # out of scope
            if not lv.isalnum():
                l += 1
                
            elif not rv.isalnum():
                r -= 1
                
            # in the scope
            else:
            
                if lv.lower() != rv.lower():
                    return False
                l += 1
                r -= 1
            
        return True
