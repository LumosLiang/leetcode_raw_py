class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # The ask here is flipping all 'O's into 'X's in that surrounded region
        
        # Any 'O' on the border of the board are not flipped to 'X'. If a border O has connection with inner            side, the whole part should also not be flipped.
        
        
        # First, deal with border, set them to False
        # Then loop all, for false, set it back to O, and for those are O, set them to X.
        
        # O(MN), O(MN)
        
    def DFS(self, board: List[List[str]]):
        w, l = len(board), len(board[0])
        
        def dfs(board, i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'o':
                board[i][j] = 'h'
                dfs(board, i+1, j)
                dfs(board, i-1, j)
                dfs(board, i, j+1)
                dfs(board, i, j-1)
        
        for x in [0, w - 1]:
            for y in range(l):
                dfs(board, x, y)
​
        for x in range(1, w - 1):
            for y in [0, l - 1]:
                dfs(board, x, y)
                
        for x in range(w):
            for y in range(l):
                if board[x][y] == "o":
                    board[x][y] = "x"
                if board[x][y] == "h":
                    board[x][y] = "o"
​
    def BFS(self, board: List[List[str]]):
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
