class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {'(':')', '{':'}', '[':']'}
        
        stack = []
        
        for i in range(len(s)):
            if stack and stack[-1] in d and d[stack[-1]] == s[i]:
                stack.pop()
            else: stack.append(s[i])
                
        if not stack: return True
        else: return False
