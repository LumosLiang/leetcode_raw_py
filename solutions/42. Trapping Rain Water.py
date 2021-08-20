class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack, res = [], 0 
        
        for right, v in enumerate(height):
            while stack and height[stack[-1]] < v:
                curr = stack.pop()
                if stack:
                    # res += w * h 
                    left = stack[-1]
                    res += (right - left - 1) * (min(v, height[left]) - height[curr])
            stack.append(right)        
        
        return res
