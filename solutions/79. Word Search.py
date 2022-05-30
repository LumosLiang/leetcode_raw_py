class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        
        # return if we can find the word since (x, y)
        def backtrack(x, y, word, cnt):
            nonlocal board
            
            if cnt == len(word):
                return True
            
            if not (0 <= x < m and 0 <= y < n and board[x][y] == word[cnt]): 
                return False
            
            val = word[cnt]
            board[x][y] = 0
            
            for i, j in [x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1]:
                temp = backtrack(i, j, word, cnt + 1)
                if temp: return True
                    
            board[x][y] = val
            return False
            
        for i in range(m):
            for j in range(n):
                
                temp = backtrack(i, j, word, 0)
                
                if temp: return True
        
        return False
        
class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
        
        
        
        
