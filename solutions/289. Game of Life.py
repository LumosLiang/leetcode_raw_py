class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """   
        self.sol2(board)
    
    # O(M * N), live neighbor cnt
    # brute force. O(M * N) space
​
    def sol1(self, board):
        
        m, n = len(board), len(board[0])
        
        new_board = [[0 for i in range(n)] for j in range(m)]
        
        # return the count of the live neighbor cell of cell (i, j)
        def helper(x, y):
            nonlocal board
            res = 0
        
            for i, j in [x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1],[x - 1, y - 1],[x + 1, y + 1],[x - 1, y + 1],[x + 1, y - 1]:
                if 0 <= i < m and 0 <= j < n and board[i][j] == 1: 
                    res += 1
            
            return res
        
        for i in range(m):
            for j in range(n):
                cnt = helper(i, j)
                if board[i][j]:
                    if cnt < 2: new_board[i][j] = 0
                    elif cnt in [2, 3]: new_board[i][j] = 1
                    elif cnt > 3: new_board[i][j] = 0
                else:
                    if cnt  == 3: new_board[i][j] = 1
        
        for i in range(m):
            for j in range(n):
                board[i][j] = new_board[i][j]  
    
    def sol2(self, board):
        m, n = len(board), len(board[0])
        
        # return the count of the live neighbor cell of cell (i, j)
        def helper(x, y):
            nonlocal board
            res = 0
        
            for i, j in [x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1],[x - 1, y - 1],[x + 1, y + 1],[x - 1, y + 1],[x + 1, y - 1]:
                if 0 <= i < m and 0 <= j < n and board[i][j] in [1, -2]: 
                    res += 1
            
            return res
        
        # introduce a third-state and forth state?
        # 0 -> 1: 2, it is now 1, but previously 0
        # 1 -> 0: -2, it is now 0, but previously 1
        
        for i in range(m):
            for j in range(n):
                cnt = helper(i, j)
                if board[i][j]:
                    if cnt < 2: board[i][j] = -2
                    elif cnt in [2, 3]: board[i][j] = 1
                    elif cnt > 3: board[i][j] = -2
                else:
                    if cnt  == 3: board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == -2: board[i][j] = 0
