class Solution:
    def searchMatrix(self, matrix, target):
        
        if matrix.count([]) == len(matrix): return False
​
        mid_0 = 0 + (len(matrix) - 1 - 0) // 2
        mid_1 = 0 + (len(matrix[0]) - 1 - 0) // 2
        
        if matrix[mid_0][mid_1] > target:
            
            matrix_diag = [m[:mid_1] for m in matrix[:mid_0]]
            matrix_left = [m[:mid_1] for m in matrix[mid_0:]]
            matrix_up = [m[mid_1:] for m in matrix[:mid_0]]
            
            return self.searchMatrix(matrix_diag, target) or self.searchMatrix(matrix_left, target) or self.searchMatrix(matrix_up, target)
        
        elif matrix[mid_0][mid_1] < target:
            
            matrix_diag = [m[mid_1 + 1:] for m in matrix[mid_0 + 1:]]
            matrix_right = [m[mid_1 + 1:] for m in matrix[:mid_0 + 1]]
            matrix_down = [m[:mid_1+1] for m in matrix[mid_0 + 1:]]
                  
            return self.searchMatrix(matrix_diag, target) or self.searchMatrix(matrix_right, target) or self.searchMatrix(matrix_down, target)
        else:
            return True
        
        return False
