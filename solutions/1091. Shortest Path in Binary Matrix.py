class Solution:
    def shortestPathBinaryMatrixTLE(self, grid: List[List[int]]) -> int:
        
        
        # typical backtrack problem
        # start from the origianl to the end
        # choices is 8-directionally connected cell as long as, its value is 0
        # path is each cell's coordinate
        # compute the count in each choose, and when reach the end, compare
        
        l = len(grid)
        
        if grid[0][0] == 1 or grid[l - 1][l - 1] == 1:
            return -1
        
        self.res = float('inf')
        grid[0][0] = 1
        
        def backtrack(grid, x, y, cnt, targetx, targety):
            
            if x == targetx and y == targety:
                self.res = min(self.res, cnt)
                return
            
            for i, j in [x + 1, y],[x - 1, y],[x, y - 1],[x, y + 1],[x + 1, y + 1],[x - 1, y + 1],[x - 1, y - 1],[x + 1, y - 1]:
                if 0 <= i < l and 0 <= j < l and grid[i][j] == 0:
                    grid[i][j] = 1
                    backtrack(grid, i, j, cnt + 1, targetx, targety)  
                    grid[i][j] = 0
                    
        backtrack(grid, 0, 0, 1, l - 1, l - 1)
        return self.res if self.res != float('inf') else -1
    
    def shortestPathBinaryMatrixTLE(self, grid: List[List[int]]) -> int:
            
        l = len(grid)
        
        if grid[0][0] == 1 or grid[l - 1][l - 1] == 1:
            return -1
        
        q = collections.deque([[(0,0), 1]])
        self.res = float('inf')
        
        while q:
            (x, y), step = q.popleft()
            if x == l - 1 and y == l - 1:
                return step
            
            grid[x][y] = 1
            for i, j in [x + 1, y],[x - 1, y],[x, y - 1],[x, y + 1],[x + 1, y + 1],[x - 1, y + 1],[x - 1, y - 1],[x + 1, y - 1]:
                if 0 <= i < l and 0 <= j < l and grid[i][j] == 0:
                    q.append([(i, j), step + 1])
​
        return -1
​
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
