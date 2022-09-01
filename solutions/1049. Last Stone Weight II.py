class Solution:
    def lastStoneWeightII(self, nums: List[int]) -> int:
        
        s, l = sum(nums), len(nums)
        t = s - s // 2
        
        dp = [[0 for i in range(t + 1)] for j in range(l)]
        
        # for i in range(l): dp[i][0] = 0
        
        for i in range(1, t + 1):
            if nums[0] <= i:
                dp[0][i] = nums[0]
        
        for i in range(1, l):
            for j in range(1, t + 1):
                if nums[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
        
        # print(dp)
        
        return abs(s - dp[l - 1][t] * 2)
        
        
#     [[0, 0], 
#      [0, 0]]
​
