class Solution:
    def isValid(self, s: str) -> bool:
        
        if s == "": return False
        
        d = {'(':')','{':'}','[':']'}
​
        stack = []
        
        for char in s:        
            if stack and stack[-1] in d and char == d[stack[-1]]:
                stack.pop()
            else:
                stack.append(char)
        
        return not stack
            
            
            
            
