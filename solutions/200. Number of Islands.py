class Solution:
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        
        res = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    
                    q = collections.deque([[i,j]])
                    grid[i][j] = '0'
                    
                    while q:
                        x,y = q.popleft()    
                        for l, k in [x, y + 1],[x, y - 1],[x - 1, y],[x + 1, y]:
                            if 0 <= l <= m - 1 and 0 <= k <= n - 1 and grid[l][k] == '1':
                                grid[l][k] = '0'
                                q.append([l, k])
                
        return res
​
    def numIslandsBFSTLE(self, grid: List[List[str]]) -> int:
        
        res = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    
                    q = collections.deque([[i,j]])
                    while q:
                        x,y = q.popleft()    
                        grid[x][y] = '0'
                        for l, k in [x, y + 1],[x, y - 1],[x - 1, y],[x + 1, y]:
                            if 0 <= l <= m - 1 and 0 <= k <= n - 1 and grid[l][k] == '1':
                                q.append([l, k])
                
        return res
    
   
    def numIslandsDFS1(self, grid: List[List[str]]) -> int:
        
        res = 0
        m = len(grid)
        n = len(grid[0])
    
        def DFS(x, y):
            for l, k in [x, y + 1],[x, y - 1],[x - 1, y],[x + 1, y]:
                if 0 <= l <= m - 1 and 0 <= k <= n - 1 and grid[l][k] == '1':
                    grid[l][k] = '0'
                    DFS(l, k)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    
                    grid[i][j] = '0'
                    DFS(i, j)
                    
        return res
    
    def numIslandsDFS2(self, grid: List[List[str]]) -> int:
        
        res = 0
        m = len(grid)
        n = len(grid[0])
