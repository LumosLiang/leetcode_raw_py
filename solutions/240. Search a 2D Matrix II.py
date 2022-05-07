class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # binary search Tree in matrix
        
        # O(m + n), O(1)
        
        m, n = len(matrix), len(matrix[0])
        
        x, y = 0, n - 1
        
        while 0 <= x < m and 0 <= y < n:
            
            if matrix[x][y] == target: return True
            if matrix[x][y] < target:
                x += 1
            else:
                y -= 1
                
        
        return False
            
        
        
