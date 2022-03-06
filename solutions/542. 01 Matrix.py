class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        return self.updateMatrixBFS(matrix)
    
    # O(MN), O(MN)
    # Still can be applied with out more space except the q
    def updateMatrixBFS(self, matrix: List[List[int]]) -> List[List[int]]:
    
        w, l = len(matrix), len(matrix[0])
        q = collections.deque()
​
        for i in range(w):
            for j in range(l):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = -1
        
        while q:
            x, y = q.popleft()
            
            for nx, ny in [x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1]:
                if 0 <= nx < w and 0 <= ny < l and matrix[nx][ny] == -1:
                    visited.add((nx, ny))
                    res[nx][ny] = res[x][y] + 1
                    q.append((nx, ny))
              
        return matrix
    
    def updateMatrixBFS(self, matrix: List[List[int]]) -> List[List[int]]:
    
        
        w, l = len(matrix), len(matrix[0])
       
        res = [[None for dummy_col in range(l)] for dummy_row in range(w)]
        visited = set()
        q = collections.deque()
​
        for i in range(w):
            for j in range(l):
                if matrix[i][j] == 0:
