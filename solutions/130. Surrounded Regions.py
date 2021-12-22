        
        for x in [0, w - 1]:
            for y in range(l):
                dfs(board, x, y)
​
        for x in range(1, w - 1):
            for y in [0, l - 1]:
                dfs(board, x, y)
                
        for x in range(w):
            for y in range(l):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "H":
                    board[x][y] = "O"
                    
    
    def solveBFS(self, board: List[List[str]]) -> None:
    
        w, l = len(board), len(board[0])
        
        q = collections.deque()
        
        for i in range(w):
            for j in range(l):
                if (i in [0, w - 1] or j in [0, l - 1]) and board[i][j] == "O":
                    q.append((i,j))
                    
        while q:
            x, y = q.popleft()
            if board[x][y] != "H":
                board[x][y] = "H"
                for nx, ny in [x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1]:
                    if  0 <= nx < w and 0 <= ny < l and board[nx][ny] == 'O':
                        q.append((nx, ny))
        
        for x in range(w):
            for y in range(l):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "H":
                    board[x][y] = "O"
        
    def solve(self, board: List[List[str]]) -> None:
    
        w, l = len(board), len(board[0])
        
        def bfs(board, x, y):
            q = collections.deque([(x, y)])
            while q:
                x, y = q.popleft()
                board[x][y] = "H"
                for nx, ny in [x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1]:
                    if  0 <= nx < w and 0 <= ny < l and board[nx][ny] == 'O':
                        q.append((nx, ny))
        
        for x in [0, w - 1]:
            for y in range(l):
                if board[x][y] == "O":
                    bfs(board, x, y)
​
        for x in range(1, w - 1):
            for y in [0, l - 1]:
                if board[x][y] == "O":
                    bfs(board, x, y)
                
        for x in range(w):
            for y in range(l):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "H":
                    board[x][y] = "O"
​
    
    def solveTLE(self, board: List[List[str]]) -> None:
​
        w, l = len(board), len(board[0])
        visited = [[False for i in range(l)] for j in range(w)]
        
        for x in range(1, w - 1):
            for y in range(1, l - 1):
                
                if not visited[x][y] and board[x][y] == "O":
                    
                    temp_coord, board_reached = [], False
                    q = collections.deque([(x,y)])
                    
                    while q:
