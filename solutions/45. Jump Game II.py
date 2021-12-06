class Solution:
    def jump1(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)
        
        for i in range(1, len(nums)):
            temp = 10001
            for j in range(i):
                if nums[j] >= i - j:
                    temp = min(temp, 1 + dp[j])
                    break
            dp[i] = temp
        return dp[-1]
    
    def jump(self, nums: List[int]) -> int:
        
        start, end, step = 0, 0, 0
        
        while end < len(nums) - 1:
            step += 1
            furthest = 0
            for j in range(start, end + 1):
                # if nums[j] + j >= len(nums) - 1:
                #     return step
                furthest = max(furthest, nums[j] + j)
            start, end = end + 1, furthest
        
        return step
            
 
