class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        return self.IsValidCol(board) and self.IsValidRow(board) and self.IsValidCube(board)
    
    
    def IsValidCol(self, board):
        
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(board[j][i])
            if not self.IsValidUnit(temp): return False
        
        return True
        
    def IsValidRow(self, board):
        for i in range(9):
            if not self.IsValidUnit(board[i]): return False
        
        return True
    
    def IsValidCube(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                
                temp = []
                
                for k in range(i, i + 3):
                    for m in range(j, j + 3):
                        temp.append(board[k][m])
                if not self.IsValidUnit(temp): return False
        
        return True
    
    def IsValidUnit(self, lst):
        
        not_empty = []
        
        for s in lst:
            if s != ".": not_empty.append(s)
                
        return len(set(not_empty)) == len(not_empty)
