class Solution:
    def decodeString(self, s: str) -> str:
        
        return self.sol1(s)
        
    def sol1(self, s):
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                # for "["
                stack.pop()
                freq, base = 0, 1
                while stack and "0" <= stack[-1] <= "9":
                    freq += base * int(stack.pop())
                    base *= 10
               
                stack.append(freq * temp)
                
        return "".join(stack)
            
                    
    def sol2(self, s):
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
        
