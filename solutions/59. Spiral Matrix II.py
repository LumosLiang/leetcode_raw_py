class Solution:
    def generateMatrix(self, n: int):
        
        x, y, dx, dy = 0, 0, 1, 0
        val = 1
        res = [[0 for i in range(n)] for j in range(n)]
        visited = set()
        
        while val < n ** 2 + 1:
            
            if not 0 <= x + dx < n or not 0 <= y + dy < n or (y + dy, x + dx) in visited:
                dx, dy = -dy, dx
            
            res[y][x] = val
            visited.add((y, x))
            
            x, y = x + dx, y + dy
            val += 1
        
        return res
