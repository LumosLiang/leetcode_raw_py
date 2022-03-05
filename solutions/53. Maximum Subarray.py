class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.DC(nums)
#         This is a really good DP problem, like the high-vote solution mentioned: "The format of the sub problem can be helpful when we are trying to come up with the recursive relation."
        
#         subproblem or the state here is:
        
#           maximum val of dp[:i], 
        
#         so the dp function is:
        
#           dp[:i] = A[i] + dp[:i - 1] if dp[:i - 1] > 0 else 0
        
#         The base here is:
        
#           dp[0] = nums[0]
    
    # O(N), O(1)
    def DP(self, nums):
        if len(nums) == 1:return nums[0]
    
        res, pre = nums[0], nums[0]
    
        for i in range(1, len(nums)):
            curr = nums[i] + (0 if pre < 0 else pre)
            pre = curr
            res = max(res, curr)
            
        return res
    
    # O(NlogN), O(logN)
    def DC(self, nums):
        
        if len(nums) == 0: return float(-inf)
        if len(nums) == 1: return nums[0]
        
        low, high = 0, len(nums) - 1
        mid = low + (high - low) // 2
        
        left = self.DC(nums[:mid])
        right = self.DC(nums[mid + 1:])
        middle = self.helper(nums, mid, low, high)
        
        return max(middle, right, left)
        
    def helper(self, nums, m, l, h):
        res = nums[m]
        
        rsum = float("-inf")  
        Sum = 0
        for i in range(m + 1, h + 1):
            Sum += nums[i]
            rsum = max(rsum, Sum)
            
        lsum = float("-inf")  
        Sum = 0
        for j in range(m - 1, l - 1, -1):
            Sum += nums[j]
            lsum = max(lsum, Sum)
                
        return max(res, res + lsum, res + rsum, res + lsum + rsum)
