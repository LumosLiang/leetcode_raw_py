class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        stack, res = [-1], 0
        
        for i, height in enumerate(heights):
            while heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        
        return res
    
​
