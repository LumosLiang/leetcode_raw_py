class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])
        
        l, r, u, d = 0, n - 1, 0, m - 1
        
        res = []
        
        while True:
        
            for i in range(l, r + 1):
                res.append(matrix[l][i])
​
            u += 1
            if u > d: break
​
            for i in range(u, d + 1):
                res.append(matrix[i][r])
​
            r -= 1
            if r < l: break
​
            for i in range(r, l - 1, -1):
                res.append(matrix[d][i])
​
            d -= 1
            if d < u: break
​
            for i in range(d, u - 1, -1):
                res.append(matrix[i][l])
​
            l += 1
            if l > r: break
        
        
        return res
