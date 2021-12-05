class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        l = len(nums)
        dp = [0] * l
        
        dp[0] = nums[0]
​
        for i in range(1, l - 1):
            
            if dp[i - 1] < i: return False
            
            dp[i] = max(i + nums[i], dp[i - 1])
            
            if dp[i] >= l - 1: return True
            
        return dp[l - 2] >= l - 1
    
    
    def canJumpWrong(self, nums: List[int]) -> bool:
        
    
        dp = [False] * len(nums)
        
        if nums[0] == 0: 
            if len(nums) == 1: return True
            else: return False
        else:
            dp[0] = True
            
            for i in range(1, len(nums)):
                temp = False
                
                for j in range(0, i):
                    temp |= dp[j] and (nums[j] > (i - j - 1))
                
                if not temp: return False
                dp[i] = temp
        
        return dp[-1]
