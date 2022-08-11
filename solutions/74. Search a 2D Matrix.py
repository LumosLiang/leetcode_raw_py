class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None: return False
        
        w = len(matrix)
        l = len(matrix[0])
        
        low = 0
        high = w * l - 1
        
        while low < high:
            mid = (low + high) // 2
           
            if matrix[mid // l][mid % l] < target:
                low = mid + 1
            else:
                high = mid
        
        return matrix[low // l][low % l] == target
​
    def 
        if matrix is None: return False
        
        w = len(matrix)
        l = len(matrix[0])
        
        low = 0
        high = w * l - 1
        
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
