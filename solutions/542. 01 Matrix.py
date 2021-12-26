class Solution:
    def updateMatrixOld(self, matrix: List[List[int]]) -> List[List[int]]:
    
        # has a value map wiht None, each cell: coordinate
        width = len(matrix[0])
        height = len(matrix)
        distance_lst = [[None for dummy_col in range(width)] for dummy_row in range(height)]
        matrix_isvisited = [[False for dummy_col in range(width)] for dummy_row in range(height)]
        Q = []
​
        
        # DFS/BFS when adjacent and itself is not zero
        
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    Q.insert(0, (i,j))
                    distance_lst[i][j] = 0
                    matrix_isvisited[i][j] = True
        
        # BFS
        while Q:
            temp_cell = Q.pop()
            if temp_cell[0] - 1 >= 0 and not matrix_isvisited[temp_cell[0]-1][temp_cell[1]]:
                 Q.insert(0, (temp_cell[0]-1, temp_cell[1]))
                 distance_lst[temp_cell[0]-1][temp_cell[1]] = distance_lst[temp_cell[0]][temp_cell[1]] + 1
                 matrix_isvisited[temp_cell[0]-1][temp_cell[1]] = True
            if temp_cell[0] + 1 < height and not matrix_isvisited[temp_cell[0]+1][temp_cell[1]]:
                 Q.insert(0, (temp_cell[0]+1, temp_cell[1]))
                 distance_lst[temp_cell[0]+1][temp_cell[1]] = distance_lst[temp_cell[0]][temp_cell[1]] + 1
                 matrix_isvisited[temp_cell[0]+1][temp_cell[1]] = True
            if temp_cell[1] - 1 >= 0 and not matrix_isvisited[temp_cell[0]][temp_cell[1]-1]:
                 Q.insert(0, (temp_cell[0], temp_cell[1]-1))
                 distance_lst[temp_cell[0]][temp_cell[1]-1] = distance_lst[temp_cell[0]][temp_cell[1]] + 1
                 matrix_isvisited[temp_cell[0]][temp_cell[1]-1] = True
            if temp_cell[1] + 1 < width and not matrix_isvisited[temp_cell[0]][temp_cell[1]+1]:
                 Q.insert(0, (temp_cell[0], temp_cell[1]+1))
                 distance_lst[temp_cell[0]][temp_cell[1]+1] = distance_lst[temp_cell[0]][temp_cell[1]] + 1
                 matrix_isvisited[temp_cell[0]][temp_cell[1]+1] = True
                    
              
        return distance_lst
        
        
        
    def updateMatrixBFS(self, matrix: List[List[int]]) -> List[List[int]]:
    
        
        w, l = len(matrix), len(matrix[0])
       
        res = [[None for dummy_col in range(l)] for dummy_row in range(w)]
        visited = set()
        q = collections.deque()
​
        for i in range(w):
            for j in range(l):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    res[i][j] = 0
                    visited.add((i, j))
        
        while q:
            x, y = q.popleft()
            
            for nx, ny in [x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1]:
                if 0 <= nx < w and 0 <= ny < l and  (nx, ny) not in visited:
                    visited.add((nx, ny))
                    res[nx][ny] = res[x][y] + 1
                    q.append((nx, ny))
              
        return res
    
    
    def updateMatrixDFSincorrect(self, matrix: List[List[int]]) -> List[List[int]]:
    
        
        w, l = len(matrix), len(matrix[0])
       
        res = [[None for dummy_col in range(l)] for dummy_row in range(w)]
        visited = set()
​
        def DFS(x, y):
            
            for nx, ny in [x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1]:
                if 0 <= nx < w and 0 <= ny < l and  (nx, ny) not in visited:
                    visited.add((nx, ny))
                    res[nx][ny] = res[x][y] + 1
                    DFS(nx, ny)
​
        for i in range(w):
            for j in range(l):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    visited.add((i, j))
                    DFS(i, j)
​
        return res
        
