class Solution:
    def calculate(self, s: str) -> int:
        
        "(2-1) + 2"
        stack, p = [], 0
        
        while p < len(s):
            if s[p] == " ": 
                p += 1
            elif s[p] in ["+", "-", "("]: 
                stack.append(s[p])
                p += 1
            elif "0" <= s[p] <= "9":
                temp = ""
                while p < len(s) and "0" <= s[p] <= "9":
                    temp += s[p]
                    p += 1
                stack.append(temp)
            else:
                temp = 0
                while stack and stack[-1] != "(":
                    num, sign = stack.pop(), stack.pop()
                    if sign == "+":
                        temp += int(num)
                    elif sign == "-":
                        temp += -int(num)
                    elif sign == "(":
                        temp += int(num)
                        break
                        
                if stack and stack[-1] == "(": stack.pop()
                stack.append(temp)
                p += 1
       
        if stack[0] == "-": stack = [0] + stack
        
        res = int(stack[0])
        for i in range(1, len(stack) - 1):
            sign = stack[i]
            if sign not in ["+", "-"]: continue
            nxt = int(stack[i + 1])
            if sign == "+":
                res = res + nxt
            elif sign == "-":
                res = res - nxt
            
                
        return res
            #"2-4-(8+2-6+(8+4-(1)+8-10))"
