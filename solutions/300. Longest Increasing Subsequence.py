class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    
        return self.DP4(nums)
    
    def backtrack(self, nums):
        memo = {}
        def DFS(nums, idx):
            
            if idx == len(nums) - 1:
                return 1
            
            if idx not in memo:
                memo[idx] = 1
                for i in range(idx + 1, len(nums)):
                    if nums[i] > nums[idx]:
                        memo[idx] = max(memo[idx], DFS(nums, i) + 1)
                
            return memo[idx]
        
        res = [DFS(nums, i) for i in range(len(nums))]
        return max(res)
    
    # O(N^2), O(N)
    def DP_forward(self, nums):
        # dp[i]'s state: the LIS of the nums[:i + 1]
        # function: dp[i + 1] = max(max([dp[j] + 1 for j in range(0, i) if nums[i + 1] > nums[j]]), 1)
        # base: dp[0] = 1
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            temp = [dp[j] + 1 for j in range(0, i) if nums[i] > nums[j]]
            if temp:
                dp[i] = max(temp)
        
        return max(dp)

    def DP_backward(self, nums):  
        # dp[i]'s state: the LIS of the nums[i:]
        # function: dp[i - 1] = max(max([dp[j] + 1 for j in range(i, len(nums)) if nums[i - 1] < nums[j]]), 1)
        # base： dp[-1] = 1
        
        # O(N * N), O(N)
    
        dp = [1] * len(nums)
        
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    # O(NlogN), O(N)
    def DP3(self, nums):
        
        LIS = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] > LIS[-1]:
                LIS.append(nums[i])
            else:
                l, r = 0, len(LIS) - 1
                while l < r:
                    mid = (l + r) // 2
                    if LIS[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid
                
                LIS[l] = nums[i]
            
        return len(LIS) 

        
    # [10,9,2,5,1,7,101,18]
    # with compute the actual LIS under O(N*N), O(N ^ 2)
    def DP4(self, nums):
        
        dp = [[num] for num in nums]
        
        for i in range(1, len(nums)):
            temp, longest = -1, []
            for j in range(i):
                if nums[j] < nums[i] and len(dp[j]) > temp:
                    longest = dp[j]
                    temp = len(dp[j])
            if temp != -1:
                dp[i] = longest + dp[i]
            
        max_len = 0
        res = []
        for i in range(len(dp)):
            if len(dp[i]) > max_len:
                res = dp[i]
                max_len = len(dp[i])
        
        return len(res)
