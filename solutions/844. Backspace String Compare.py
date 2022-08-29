class Solution:
    def backspaceCompare1(self, s: str, t: str) -> bool:
         
        def helper(s):
            stack = []
            
            for c in s:
                if c == "#":
                    if stack: stack.pop()
                else:
                    stack.append(c)
        
            return stack
        
        return helper(s) == helper(t)
    
    
#     1. two pointers
#     2. two cnts
#     3. make sure we compare the actually value
#         (as long as next is #, add till next is not #
#         as long as next is not # and # has value, we used it at once)
​
#         as long as next is not # and # is None, we start to compare:
#             if not equal: return False
#             if equal, continue
    
#     if not finshed in the same time, it is actually false 
    
    def backspaceCompare(self, s: str, t: str) -> bool:
         
        p1, p2, cnts, cntt = len(s) - 1, len(t) - 1, 0, 0
        
        while p1 >= 0 or p2 >= 0:
            
            while p1 >= 0:
                if s[p1] == "#":
                    p1 -= 1
                    cnts += 1
                elif s[p1] != "#" and cnts > 0:
                    p1 -= 1
                    cnts -= 1
                else: break
                
            while p2 >= 0:
                if t[p2] == "#":
                    p2 -= 1
                    cntt += 1
                elif t[p2] != "#" and cntt > 0:
                    p2 -= 1
                    cntt -= 1
                else: break
                
            if (p1 < 0 and p2 >= 0) or (p1 >= 0 and p2 < 0):
                return False
            
            if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False
            
            
            
            p1 -= 1
            p2 -= 1
        
        return True
    
    
​
    
