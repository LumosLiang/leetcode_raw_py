class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # pure DP problem
        # dp[i][j] = min(dp[i - 1][j], dp[i][j]) + triangle[i][j]
        
        init = triangle[0][0]
        
        l = len(triangle)
        
        if l == 1: return init
        
        dp = [init]
        
        for i in range(1, l):
            temp = []
            for j in range(len(triangle[i])):
                if j == 0: temp.append(dp[0] + triangle[i][j])
                elif j == len(triangle[i]) - 1: temp.append(dp[j - 1] + triangle[i][j])
                else: temp.append(min(dp[j - 1], dp[j]) + triangle[i][j])
            dp = temp
            print(dp)
            
        return min(dp)
