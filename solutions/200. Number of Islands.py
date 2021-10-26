class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
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
