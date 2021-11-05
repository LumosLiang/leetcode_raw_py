class Solution:
<<<<<<< HEAD
    def isValid(self, s: str) -> bool:

        stack = []
        hash = {'(': ')', '{': '}', '[': ']'}

        for item in s:
            if stack and stack[-1] in hash and hash[stack[-1]] == item:
                stack.pop()
                continue
            stack.append(item)

        return not stack
=======
    def isValid(self, s: str) -> bool:
        
        d = {'(':')', '{':'}', '[':']'}
        
        stack = []
        
        for i in range(len(s)):
            if stack and stack[-1] in d and d[stack[-1]] == s[i]:
                stack.pop()
            else: stack.append(s[i])
                
        if not stack: return True
        else: return False
>>>>>>> 1870dd3c764dee6f244fb461499fe34e38527ffd
