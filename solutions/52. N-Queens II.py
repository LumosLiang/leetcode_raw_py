class Solution:
    def totalNQueens(self, n: int) -> int:
​
        res, choices = [], []
        
        for i in range(n):
            for j in range(n):
                choices.append((i,j))
                
        board = [["" for _ in range(n)] for _ in range(n)]
        
        def backtrack(choices, board, queencnt, cnt):
            if not choices and queencnt == cnt:
                temp = ["".join(b) for b in board]
                res.append(temp)
                return
            
            for i in range(len(choices)):
                m, n = choices[i]
                board[m][n] = "Q"
                
                new_choices = []
                for item in choices[i + 1:]:
                    x, y = item[0], item[1]
                    if x == m or y == n or (abs(x - m) == abs(y - n)):
                        board[x][y] = "."
                    else:
                        new_choices.append((x, y))

                backtrack(new_choices, board, queencnt + 1, cnt)
                board[m][n] = "."
                
        backtrack(choices, board, 0, n)
        return len(res)

       
class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def check(board, choice_idx):
            for i in range(n):
                if i != choice_idx and board[i] != -1:
                    if board[choice_idx] == board[i] or abs(board[i] - board[choice_idx]) == abs(i - choice_idx):
                        return False
            return True
        
        res = 0
        
        def dfs(i, board):
            nonlocal res
            if i == n:
                res += 1
                return
                
            for j in range(n):
                board[i] = j
                if check(board, i):
                    dfs(i + 1, board)
                board[i] = -1
                
        dfs(0, [-1] * n)
        return res
