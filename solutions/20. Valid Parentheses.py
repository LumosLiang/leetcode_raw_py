d = {'(':')','{':'}','[':']'}
​
class Solution:
    def isValid(self, s: str) -> bool:
        if s == "": return False
        
        s = list(s)
        stack = []
        
        while s:
            if stack and stack[-1] in d:
                if s[0] == d[stack[-1]]:
                    stack.pop()
                    s.pop(0)
                else:
                    stack.append(s.pop(0))
            else:
                stack.append(s.pop(0))
        
        return not stack
            
            
            
            
