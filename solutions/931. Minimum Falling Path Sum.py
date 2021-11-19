class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        # base case: dp(0, j) = matrix[0][j]
        # state: current path sum at coordinate (i, j)
        # choice: dp(i, j) = min(dp(i - 1, j - 1), dp(i - 1, j), dp(i - 1, j + 1)) + matrix[i][j]
        
        # return self.bruteforce(matrix)
        # return self.memo(matrix)
        return self.dp(matrix)
        
    # Brute-force recursion -> TLE    
    def bruteforce(self, matrix):
        l = len(matrix)
        res = float('inf')
        
        def helper(i, j):
            
            # out of matrix
            if i < 0 or j < 0 or i > l - 1 or j > l - 1: return 10002
            
            # base
            if i == 0: return matrix[0][j]
            
            # recursion
            return min(helper(i - 1, j - 1), helper(i - 1, j), helper(i - 1, j + 1)) + matrix[i][j]
        
        for j in range(l):
            res = min(res, helper(l - 1, j))
            
        return res
​
​
    # recursion with memo
    def memo(self, matrix):
        l = len(matrix)
        res = float('inf')
        memo = [[10001 for j in range(l)] for i in range(l)]
        
        def helper(i, j):
​
            if i < 0 or j < 0 or i > l - 1 or j > l - 1: return 10002
​
            if i == 0: return matrix[0][j]
            
            # memo
            if memo[i][j] != 10001: return memo[i][j]
            
            memo[i][j] = min(helper(i - 1, j - 1), helper(i - 1, j), helper(i - 1, j + 1)) + matrix[i][j]
            return memo[i][j]
        
        for j in range(l):
            res = min(res, helper(l - 1, j))
            
        return res
​
    # dp -> bottom up
    def dp(self, matrix):
​
        l = len(matrix)
       
        for i in range(l):
            for j in range(l):
                if i != 0:
                    # edge case 1
                    if j == 0:
                        matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j + 1])
                    # edge case 2
                    elif j == l - 1:
                        matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j - 1])
                    else:
                        matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j + 1], matrix[i - 1][j - 1])
        
        return min(matrix[-1])
​
