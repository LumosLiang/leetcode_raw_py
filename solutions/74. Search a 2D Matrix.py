class Solution:
    def searchMatrix(self, matrix, target):
        
        if matrix is None: return False
        
        w = len(matrix)
        l = len(matrix[0])
        
        low = 0
        high = (w - 1) * l + l - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            # mid_coord = [mid // w, mid % w - 1]
            
            if matrix[mid // l][mid % l] < target:
                low = mid + 1
            elif matrix[mid // l][mid % l] > target:
                high = mid - 1
            else:
                return True
        return False
