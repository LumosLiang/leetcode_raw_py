class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
         
        def helper(string):
            
            ls = list(string)
            stack = []
            
            while ls:
                temp = ls.pop()
                if stack and stack[-1] == "#" and temp != "#":
                    stack.pop()
                else:
                    stack.append(temp)
            
            return "".join([i if i != "#" else  "" for i in stack]) if stack else ""
        
        return helper(s) == helper(t)
