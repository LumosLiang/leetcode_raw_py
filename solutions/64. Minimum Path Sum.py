class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
​
        return self.BFS(grid)
        
    # all about backtrack/DFS/recursion
    def sol0(self, grid):
        # every step has two choices
        m, n = len(grid), len(grid[0])
        
        def backtrack(i, j):
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            if j == n - 1 and 0 <= i < m - 1:
                return grid[i][j] + backtrack(i + 1, j)
            
            if i == m - 1 and 0 <= j < n - 1:
                return grid[i][j] + backtrack(i, j + 1)
            
            if 0 <= j < n - 1 and 0 <= i < m - 1:
                return grid[i][j] + min(backtrack(i + 1, j), backtrack(i, j + 1))
        
        return backtrack(0, 0)
        
    # recursion with memo
        
    def memo1(self, grid):
        # every step has two choices
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def backtrack(i, j):
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            if j == n - 1 and 0 <= i < m - 1:
                return grid[i][j] + backtrack(i + 1, j)
            
            if i == m - 1 and 0 <= j < n - 1:
                return grid[i][j] + backtrack(i, j + 1)
            
            if 0 <= j < n - 1 and 0 <= i < m - 1:
                return grid[i][j] + min(backtrack(i + 1, j), backtrack(i, j + 1))
        
        return backtrack(0, 0)
    
    def memo2(self, grid):
        # every step has two choices
        m, n = len(grid), len(grid[0])
        
        memo = {}
        def backtrack(i, j):
            
            if (i,j) in memo: return memo[(i,j)]
            
            memo[(i,j)] = -1
            if i == m - 1 and j == n - 1:
                memo[(i,j)] = grid[i][j]
            
            if j == n - 1 and 0 <= i < m - 1:
                memo[(i,j)] = grid[i][j] + backtrack(i + 1, j)
            
            if i == m - 1 and 0 <= j < n - 1:
                memo[(i,j)] = grid[i][j] + backtrack(i, j + 1)
            
            if 0 <= j < n - 1 and 0 <= i < m - 1:
                memo[(i,j)] = grid[i][j] + min(backtrack(i + 1, j), backtrack(i, j + 1))
            
            return memo[(i,j)]
        
        return backtrack(0, 0)
    
    # DP backward, forward. 
    
    def forward(self, grid):
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
