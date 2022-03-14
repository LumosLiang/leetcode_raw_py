class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # additinal space
       
        # coordinate relationship
        # first
        # [0,0], [0,n-1], [n-1,n-1], [n-1,0]
        # [0,0 + 1], [0 + 1, n-1], [n-1, (n-1) - 1], [(n-1) - 1, 0]
        # [0,0 + 2], [0 + 2, n - 1], [n-1, (n-1) - 2], [(n-1) - 2, 0]
        # [0, 0 + n - 2], [0 + n - 2, n-1], [n-1, (n-1) - (n - 2)], [(n-1) - (n - 2), 0]
        
        # second - level
        # [1,1], [1,n-1 - 1], [n - 1 - 1,n - 1 - 1], [n-1 - 1,1]
        # [1,1 + 1], [1 + 1, n - 1 - 1], [n - 1 - 1, (n-1) - 1 - 1], [(n-1) - 1 - 1, 1]
        # [1, n - 3], [n - 3, n - 1 - 1], [n - 1 - 1, (n - 1 - 1) - (n - 3)], [(n-1) - (n - 2), 0]
        
        # i level
        # [i, i], [i, n - 1 - i], [n - 1 - i, n - 1 - i], [n - 1 - i, i]
        
        # [i, n - i - 2], [n - i - 2, n - 1 - i], [n - 1 - i, n - 1 - (n - i - 2)], [n - 1 - (n - i - 2), i]
        
        n = len(matrix)
        
        for i in range(0, n // 2):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]
                
        
                
        
        
        
