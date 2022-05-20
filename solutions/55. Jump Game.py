class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.sol1(nums)
        
    # DP
    # dp[i] -> can reach the last at idx: i
    # dp[i - 1] dp[i]
    # TLE
    def sol1(self, nums):
        l = len(nums)
        dp = [False] * l
        dp[-1] = True
        
        for i in range(l - 2, -1, -1):
            if i + nums[i] >= l - 1:
                dp[i] = True
            else:
                for j in range(1, nums[i] + 1):
                    if dp[i + j]:
                        dp[i] = True
                        break
        
        return dp[0]
        
    
    # greedy O(N), O(1)
    def sol2(self, nums):
​
        # 1. at every step: 
        #   if idx <= farest, update farest.
        #   else break. return -1
        
        farest = 0
        
        for i in range(len(nums)):
            if i <= farest:
                farest = max(farest, i + nums[i])
                if farest >= len(nums) - 1:
                    return True
            else: 
                return False
        
        
