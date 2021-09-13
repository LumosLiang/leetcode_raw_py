class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1: return s
        
        res = ""
        
        for i in range(len(s)):
            temp_odd = self.helper(s, i, i)
            if len(temp_odd) > len(res): res = temp_odd
            
            temp_even = self.helper(s, i, i + 1)
            if len(temp_even) > len(res): res = temp_even
​
        return res
        
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -=1
            r += 1
        return s[l + 1:r]
            
        
        
        
