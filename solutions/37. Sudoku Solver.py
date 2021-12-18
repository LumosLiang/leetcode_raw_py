class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # find all empty cells
        self.backtrack(board, 0, 0)
        
    # backtrack(self, choice, path):  
    def backtrack(self, board, i, j):
        
        if j == 9:
            return self.backtrack(board, i + 1, 0)
        
        if i == 9:
            return True
        
        if board[i][j] != ".":
            return self.backtrack(board, i, j + 1)
    
        for choice in ["1","2","3","4","5","6","7","8","9"]:
            if not self.checks(board, i, j, choice): continue
            board[i][j] = choice
            if self.backtrack(board, i, j + 1):
                return True
            board[i][j] = "."
        
        return False
        
    def checks(self, board, x, y, choice):
        # check x 
        
        for j in range(9):
            if board[x][j] == choice:
                return False
        
        # check y
        for i in range(9):
            if board[i][y] == choice:
                return False
            
        # check 3 * 3 grid
        gx, gy = x // 3 * 3, y // 3 * 3
        for k in range(gx, gx + 3):
            for m in range(gy, gy + 3):
                if board[k][m] == choice:
                    return False
            
        return True
​
            
