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
                
        # [2, 4, 1, 6]
        
        # 如果纯从 Greedy的角度，以下方法好在哪里
        # 1. 三个参数不止存储了历史信息，还能不断更新最优的candidate，来保证后面信息的计算
        # 2. Greedy就体现在：不断更新最优的candidate
        
        smallest, largest = float('inf'), float('inf')
        
        for num in nums:
            if num > largest: return True
            
            if num < smallest:
                smallest = num
            elif num > smallest:
                largest = num
        
        return False
        
        
