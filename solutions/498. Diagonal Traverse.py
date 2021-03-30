class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # first upper-right,[-1, 1]
            # if upper-right direction exceed the y boundary, [0,1] 
            # if upper-right direction exceed the x right boundary, [1,0]
        #  then lower-left, [1, -1]
            # if lower-left direction exceed the y boundary, [0,1] 
            # if lower-left direction exceed the x boundary, [1,0]
        
        if not matrix:return []
        
        i, j = 0, 0
        w, l = len(matrix) - 1, len(matrix[0]) - 1
        flag = True
        res = [matrix[i][j]]
        
        while i <= w and j <= l:
            if flag:
                if i - 1 >= 0 and j + 1 <= l:
                    i -= 1
                    j += 1
                    res.append(matrix[i][j])
                elif i - 1 < 0 and j + 1 <= l:
                    j += 1
                    res.append(matrix[i][j])
                    flag = not flag
                elif j + 1 > l:
                    i += 1
                    if i <= w:
                        res.append(matrix[i][j])
                        flag = not flag
​
            else:
                if i + 1 <= w and j - 1 >= 0:
                    i += 1
                    j -= 1
                    res.append(matrix[i][j])
                elif i + 1 <= w and j - 1 < 0:
                    i += 1
                    res.append(matrix[i][j])
                    flag = not flag
                elif i + 1 > w:
                    j += 1
                    if j <= l:
                        res.append(matrix[i][j])
                        flag = not flag   
                    
        return res
                
            
        
            
                
            
            
            
        
