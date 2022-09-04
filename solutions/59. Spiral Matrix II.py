class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        l, r, u, d = 0, n - 1, 0, n - 1
        cnt = 1
        
        while cnt < n ** 2 + 1:
        
            for i in range(l, r + 1):
                matrix[l][i] = cnt
                cnt += 1
                
            u += 1
            for i in range(u, d + 1):
                matrix[i][r] = cnt
                cnt += 1
                
            r -= 1
            for i in range(r, l - 1, -1):
                matrix[d][i] = cnt
                cnt += 1
​
            d -= 1
            for i in range(d, u - 1, -1):
                matrix[i][l] = cnt
                cnt += 1
​
            l += 1
            
        return matrix
​
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        cnt = 1
        x, y, dx, dy = 0, 0, 0, 1
        visited = set()
        
        while cnt < n ** 2 + 1:
            
            if x + dx in [-1, n] or y + dy in [-1, n] or (x + dx, y + dy) in visited:
                dx, dy = dy, -dx 
            
            matrix[x][y] = cnt
            visited.add((x, y))
            cnt += 1
            x += dx
            y += dy
            
        return matrix
