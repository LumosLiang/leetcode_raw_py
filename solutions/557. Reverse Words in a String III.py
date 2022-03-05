class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split(" ")
        res = ""
        for i in range(len(s)):
            res += "".join(list(s[i])[::-1])
            if i < len(s) - 1:res += " "
        
        return res
            
