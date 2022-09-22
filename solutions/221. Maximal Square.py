class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        res = 0  
        m, n = len(matrix), len(matrix[0])
        histograms = [0] * n
        
        def get_largest_square(nums):
            
            ans = 0
            stack = [-1]
            nums += [-1]
            
            for i, val in enumerate(nums):
                while stack and nums[stack[-1]] > val:
                    h = nums[stack.pop()]
                    l = stack[-1]
                    w = i - l - 1
                    ans = max(ans, min(w, h) ** 2)
                    
                stack.append(i)
            
            return ans
            
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    histograms[j] += 1
                else:
                    histograms[j] = 0
                
            res = max(res, get_largest_square(histograms))
            
        return res
