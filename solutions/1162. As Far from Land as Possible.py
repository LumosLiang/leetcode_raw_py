class Solution:
    def maxDistance(self, mat: List[List[int]]) -> int:
       
        # BFS
    
        m, n = len(mat), len(mat[0])
        q = collections.deque()
        res = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
        
        while q:
            x, y = q.popleft()
            for i, j in [x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1]:
                if 0 <= i < m and 0 <= j < n and mat[i][j] == -1:
                    mat[i][j] = mat[x][y] + 1
                    res = max(res, mat[i][j])
                    q.append((i,j))
        
        return res - 1
