class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return self.DFS(grid)
        
    def BFS(self, grid):
        # loop all, and bfs all, DFS怎么统计cnt呢？
        
        res = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    
                    grid[i][j] = 0
                    area = 0
                    
                    q = collections.deque([[i,j]])
                    while q:
                        x,y = q.popleft()
                        area += 1
                        for l, k in [x, y + 1],[x, y - 1],[x - 1, y],[x + 1, y]:
                            if 0 <= l <= m - 1 and 0 <= k <= n - 1 and grid[l][k] == 1:
                                grid[l][k] = 0
                                q.append([l, k])
                                
                    res = max(res, area)
                
        return res
    
    def DFS(self, grid):
        
        # update the area start from i, j for this connected component
        # pre-order traversal
        def DFS(i, j):
            nonlocal area
            nonlocal grid
            nonlocal m
            nonlocal n
            
            if not (0 <= i < m and 0 <= j < n and grid[i][j] == 1):
                return
            
            area += 1
            grid[i][j] = 0
            
            DFS(i - 1, j)
            DFS(i + 1, j)
            DFS(i, j - 1)
            DFS(i, j + 1)  
        
        res = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    
                    area = 0
                    DFS(i, j)         
                    res = max(res, area)
                
        return res
