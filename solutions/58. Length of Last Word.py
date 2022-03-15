class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # O(N), O(1)
        
        
        r = len(s) - 1
        
        if s[r] == " ":
            while s[r] == " ":
                r -=1
        
        l = r
        while l >= 0:
            if s[l] == " ":
                break
            l -= 1
        
        return r - l
        
​
