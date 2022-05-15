class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        i = len(s) - 1
        
        while i > -1:
            if s[i] != "[":
                stack.append(s[i])
                i -= 1
            else:
                temp = ""
                j = i - 1
                
                # cnt all the numbers
                while j > -1 and "0" <= s[j] <= "9":
                    j -= 1
                cnt = s[j + 1:i]
                
                # get the current letters in recent []
                while stack[-1] != "]":
                    temp += stack.pop()
                
                # pop the recent useless "]"
                stack.pop()
                
                # append the recent result
                stack.append(temp * int(cnt))
                
                i = j
        
        return "".join(stack[::-1])
        
        
                
