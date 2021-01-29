class Solution:
    def searchMatrix(self, matrix, target):
        
        if not matrix: return False
        
        l = len(matrix[0]) - 1
        w = 0
        
        while l >= 0 and w <= len(matrix) - 1:
            if matrix[w][l] == target:
                return True
            elif matrix[w][l] > target:
                l -= 1
            elif matrix[w][l] < target:
                w += 1
            
        
        return False
​
