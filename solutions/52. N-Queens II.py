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
​
                backtrack(new_choices, board, queencnt + 1, cnt)
                board[m][n] = "."
                
        backtrack(choices, board, 0, n)
        return len(res)
