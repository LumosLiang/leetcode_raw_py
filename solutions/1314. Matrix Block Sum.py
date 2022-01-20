class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        # if go with the intuitive way, I might get TLE on this.
        # first m * N loop, and for every loop, I will get another M*N loop at most.   
        # so that will be MN*MN which is O(M2N2), will TLE
        
        # another way is maybe a memo to do this?
        
        m, n = len(mat), len(mat[0])
        
        # generate presum
        for i in range(m):    
            for j in range(n):
                if j > 0:
                    mat[i][j] += mat[i][j - 1]
            if i > 0:
                mat[i] = [mat[i][m] + mat[i - 1][m] for m in range(n)]
        
        # generate res
        res = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):      
            for j in range(n):
                x, y = i + k, j + k
                temp_sum, exclu_x, exlu_y, inclu_x_y = 0, 0, 0, 0
                
                # sum
                temp_sum = mat[min(x, m - 1)][min(y, n - 1)]
                
                # exclu_x
                x_diff = x - (2 * k + 1)
                if x_diff >= 0: exclu_x = mat[x_diff][min(y, n - 1)]
                    
                # exlu_y
                y_diff = y - (2 * k + 1)
                if y_diff >= 0: exlu_y = mat[min(x, m - 1)][y_diff]
                    
                #inclu_x_y
                if x_diff >= 0 and y_diff >= 0: inclu_x_y = mat[x_diff][y_diff]
                
                
                res[i][j] = temp_sum - exclu_x - exlu_y + inclu_x_y
        
        return res
                
                
                
