class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        return self.DFS(matrix)
        
    def DFS(self, matrix):
        
        m, n = len(matrix), len(matrix[0])
        
        memo = [[-1 for j in range(n)] for i in range(m)]
        
        # from point(i, j), return the max path I can get in this matrix
        def helper(i, j):
            
            if memo[i][j] == -1:
                
                temp = 1
                for x, y in [i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]:
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        temp = max(temp, helper(x, y) + 1)
                
                memo[i][j] = temp
                    
            return memo[i][j]
            
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, helper(i, j))
        
        return res
        
    def BFS(matrix):
        
        pass
        
        
    def DP(matrix):
        
        pass
         
