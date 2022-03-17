class Solution:
    def evalRPN(self, tokens) -> int:
        
        # O(N), O(N)
        # kept adding to stack
        # while the len(stack) >= 3 and stack [-1] and stack[-2] are number, stack[-3] are operator, 
            # pop them out with the stack[-3], compute them accoridng to the operator, and then add to the stack again.
        # else, append the token.pop()
        
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
