class Solution:
    def find132pattern(self, nums):
        
        stack, s2 = [], float('-inf')
        
        for n in nums[::-1]:
            if n < s2: return True
            while stack and stack[-1] < n:s2 = stack.pop()
            stack.append(n)
        return False
