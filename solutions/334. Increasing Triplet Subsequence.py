class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
    
        # think easier, think correct, and 一点一点优化        
        return self.sol2(nums)
        
    def TLE(self, nums):  
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                dp[i] = max(dp[i], (dp[j] + 1) if nums[j] < nums[i] else dp[i])
                if dp[i] == 3:
                    return True
​
        return False
​
    def sol2(self, nums):
                
        # O(N * log3), O(N)
    
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
            if len(LIS) == 3: return True
        
        return False
    
    def sol3(self, nums):
                
        # O(N), O(1)
    
        s, l = float('inf'), float('inf')
        
        for i in range(len(nums)):
            if nums[i] > l: return True
            if nums[i] < s: s = nums[i]
            else: l = nums[i]
        
        return False
    
                
        
        
