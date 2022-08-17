class Solution:
    def solveNQueens(self, n: int):
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
        return res
    
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def check(board, choice_idx):
            for i in range(n):
                if i != choice_idx and board[i] != -1:
                    if board[choice_idx] == board[i] or abs(board[i] - board[choice_idx]) == abs(i - choice_idx):
                        return False
            return True
        
        res = []
        
        def dfs(i, board, path):
        
            if i == n:
                res.append(path)
                return
                
            for j in range(n):
                board[i] = j
                if check(board, i):
                    temp = "."*j + "Q" + "."*(n - j - 1)
                    dfs(i + 1, board, path + [temp])
                board[i] = -1
                
        dfs(0, [-1] * n, [])
        return res

        

    
