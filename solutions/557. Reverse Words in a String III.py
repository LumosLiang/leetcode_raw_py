class Solution:
    def reverseWords(self, s: str) -> str:
    
        return self.sol2(s)
    
    def sol1(self, s):
        s = s.split(" ")
        res = ""
        for i in range(len(s)):
            res += "".join(list(s[i])[::-1])
            if i < len(s) - 1:res += " "
        
        return res
    
    def sol2(self, s):
        
        def reverse(s, left, right):
            if left >= right: return
            
            while left <= right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        s, p1, p2 = list(s) + [" "], 0, 0
​
        while p2 < len(s):
            if s[p2] != " ":
                p2 += 1
            else:
                reverse(s, p1, p2 - 1)
                p2 += 1
                p1 = p2
                
        
        return "".join(s).rstrip(" ")    
    
    
