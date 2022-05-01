class Solution:
    def calculate(self, s: str) -> int:
        # "3+20/10-1312"
        
        stack = []
        curr, pre_sign = 0, "+"
        i = 0
        l = len(s)
        
        def jump_zero(length, idx):
            while idx < length and s[idx] == " ": idx += 1
            return idx
            
        def find_num(length, idx):
            j = idx + 1
            while j < length and s[j].isdigit(): j += 1
            return j
        
        while i < l:
            i = jump_zero(l, i)
            
            if i >= l: break
            
            if s[i] in ["+", "-"]:
                if pre_sign == "+": curr += int(stack.pop())
                else: curr -= int(stack.pop())
                pre_sign = s[i]
                i += 1
                
            elif s[i] == "*":
                temp = stack.pop()
                left = jump_zero(l, i + 1)
                right = find_num(l, left)
                temp = int(temp) * int(s[left:right])
                stack.append(temp)
                i = right
                
            elif s[i] == "/":
                temp = stack.pop()
                left = jump_zero(l, i + 1)
                right = find_num(l, left)
                temp = int(temp) // int(s[left:right])
                stack.append(temp)
                i = right
            else:
                j = find_num(l, i)
                stack.append(s[i:j])
                i = j
        
        if not stack: return curr
        
        if pre_sign == "+": return curr + int(stack[-1])
        elif pre_sign == "-": return curr - int(stack[-1])
        
