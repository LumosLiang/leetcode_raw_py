class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        points = [0] * 10000
        dp = [0] * 10000
        
        for num in nums:
            points[num] += num
        
        dp[0] = points[0]
        dp[1] = max(dp[0], points[1])
        
        for i in range(2, len(points)):
            dp[i] = max(points[i] + dp[i - 2], dp[i - 1])
        
        return dp[len(points) - 1] 
