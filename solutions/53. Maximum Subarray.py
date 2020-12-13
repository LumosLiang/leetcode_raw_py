class Solution:
    def maxSubArray(self, nums):
     
        low, high = 0, len(nums) - 1
        mid = low + (high - low) // 2
        
        if nums == []:
            return float("-inf")
        if len(nums) == 1:
            return nums[0]
        
        # leftarray
        left = self.maxSubArray(nums[:mid])
        # rightarray
        right = self.maxSubArray(nums[mid + 1:])
        # mid
        middle = self.midSubArray(nums, mid, low, high)
        
        return max(middle, right, left)
        
    def midSubArray(self, nums, m, l, h):
        res = nums[m]
​
        rsum = float("-inf")  
        Sum = 0
        for i in range(m + 1, h + 1):
            Sum += nums[i]
            if Sum > rsum:
                rsum = Sum
            
        lsum = float("-inf")  
        Sum = 0
        for j in range(m - 1, l - 1, -1):
            Sum += nums[j]
            if Sum > lsum:
                lsum = Sum
​
        return max(res, res + lsum, res + rsum, res + lsum + rsum)
​
