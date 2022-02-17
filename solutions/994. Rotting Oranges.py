class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # decide BFS
        
        ## compute count and add rotten orange to q
        
        o_cnt, q = 0, collections.deque()
        
        w, l = len(grid), len(grid[0])
        
        for i in range(w):
            for j in range(l):
                if grid[i][j] != 0:
                    o_cnt += 1
                    if grid[i][j] == 2:
                        q.append([i, j])
        
        if len(q) == o_cnt: return 0
        
        ## start BFS to rotten every orange:
        
        res, rest, cnt = 0, o_cnt - len(q), 0
        
        while q:
​
            tempq = collections.deque()
            
            while q:
                curr = q.popleft()
                i, j = curr[0], curr[1]
                
                for m, n in [i + 1, j],[i - 1, j],[i, j + 1],[i, j - 1]:
                    if 0 <= m < w and 0 <= n < l and grid[m][n] == 1:
                        grid[m][n] = 2
                        cnt += 1
                        tempq.append([m, n])
                        
            res += 1
            q = tempq
                    
        
        return -1 if cnt != rest else res - 1
