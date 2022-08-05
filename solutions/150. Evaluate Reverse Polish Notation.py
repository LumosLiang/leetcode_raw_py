class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return self.sol1(tokens)
    
    def sol1(self, tokens):
        stack = []
        
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(t)
            else:
                nums1 = int(stack.pop())
                nums2 = int(stack.pop())
                temp = 0
                if t == "+":
                    temp = nums2 + nums1
                elif t == "-":
                    temp = nums2 - nums1
                elif t == "*":
                    temp = nums2 * nums1
                else:
                    temp = nums2 / nums1
                stack.append(int(temp))
            
        return stack[-1]
    
    def sol2(self, tokens):
        stack = []
        operators = {"+": 201, "-": 202, "*": 203, "/":204}
        
        while tokens or len(stack) > 1:
            if len(stack) >= 3 and stack[-1] not in operators and stack[-2] not in operators and stack[-3] in operators:
                n1, n2, o = stack.pop(), stack.pop(), stack.pop()
                n1, n2 = int(n1), int(n2)
                
                temp = 0
                if operators[o] == 201:
                    temp = n1 + n2
                elif operators[o] == 202:
                    temp = n1 - n2
                elif operators[o] == 203:
                    temp = n1 * n2 
                elif operators[o] == 204:
                    temp = n1 / n2
                
                stack.append(int(temp))
            else:
                stack.append(tokens.pop())    
        
        return stack[-1]
