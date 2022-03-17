class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        
        return self.sol2(nums, k)
        # DFS, recursion, DP
    def sol1(self, nums: List[int], k: int):
        memo = {}
        
        def dp(pop, nums, cnt):
            
            tempk = str(pop) + str(nums)
            
            if tempk in memo: return memo[tempk]
            
            # base1 -> -1
            if nums == [] and cnt == k:
                memo[tempk] = -1
            
            # base2 -> -1
            elif cnt == k:
                memo[tempk] = nums[0]
            
            elif not pop:
                memo[tempk] = dp(pop + [nums[0]], nums[1:], cnt + 1)
            
            else:
                memo[tempk] = dp(pop[1:], [pop[0]] + nums, cnt + 1)
                if len(nums) > 0:  
                    memo[tempk] = max(dp(pop + [nums[0]], nums[1:], cnt + 1), memo[tempk])
        
            return memo[tempk]
        
        return dp([], nums, 0)
​
    
    def sol2(self, nums: List[int], k: int):
       
        if k == 0: return nums[0]
            
        if len(nums) == 1: 
            if k == 1 or k % 2: return -1
            else: return nums[0]
          
        if k > len(nums): return max(nums)
        
        if k == len(nums):
            m = -1
            
            for i in range(k - 1):
                m = max(m, nums[i])
            
            return m
        
        if k < len(nums):
            m = -1
            
            for i in range(k - 1):
                m = max(m, nums[i])
            
            return max(m, nums[k])
        
        
