class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
    
    # O(N)
    def sol1(self, matrix):
        # 两种思路，一种是单调栈，一种是DP。
        # 84是 85的子问题，只不过85扩展到了2维而已
​
        m, n = len(matrix), len(matrix[0])
        
        heights = [0] * n
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
                
            res = max(res, self.largest_Rectangle(heights))
        
        return res
    
    def largest_Rectangle(self, heights):
        
        stack = [-1]
        heights.append(-1)
        res = 0
        
        for idx, val in enumerate(heights):
            
            while stack and heights[stack[-1]] > val:
                h = heights[stack.pop()]
                width = idx - stack[-1] - 1
                res = max(res, width * h)
            stack.append(idx)
            
​
        return res
