class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return self.sol3(grid)
    # why not using BFS or DFS here? introduce more complexity when you have tackle with visited cell 
    # sol1 and sol2 are actually the same
    def sol1(self, grid):
        
        m, n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    
                    temp = 0
                    for l, k in [i + 1, j],[i - 1, j],[i, j + 1],[i, j - 1]:
                        if 0 <= l < m and 0 <= k < n and grid[l][k] == 1:
                            temp += 1
​
                    res += (4 - temp)
            
        return res
    
    def sol2(self, grid):
        
        m, n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    
                    for l, k in [i + 1, j],[i - 1, j],[i, j + 1],[i, j - 1]:
                        if not (0 <= l < m and 0 <= k < n and grid[l][k] == 1):
                            res += 1
​
        return res
        
    # give a direction and count the neighbor edge   
    def sol3(self, grid):
        
        m, n = len(grid), len(grid[0])
        cnt, neighbor = 0, 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                    for l, k in [i + 1, j],[i, j + 1]:
                        if 0 <= l < m and 0 <= k < n and grid[l][k] == 1:
                            neighbor += 1
​
        return cnt * 4 - neighbor * 2
        
        
