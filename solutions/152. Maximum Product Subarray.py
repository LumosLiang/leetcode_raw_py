class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        return self.dp1(nums)
    
    def prefix(self, A):
        
        # 为什么结果一定在前缀积里面？
        
        # https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC++Python-it-can-be-more-simple/330117
        
        # 如果 subarry A[i:j] 是我们现在的状态，他们的积是P，存在以下情况：
#         1. P > 0, 
#             a. 如果i，j同号，我们就扩充到i，j.
#             b. 如果i，j异号，那我们就扩充到其中一个。
#         2. P < 0:
#             a. 如果i，j异号，那我们就扩充到其中一个。
            
#         3. P = 0:
#             reset P = 1 继续向前向后。
        
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
​
        return max(A + B)
    
    
    # 有点像maximum subarray， 但是注意这是乘法。乘法意味着两个负数，可以得到一个更大的数字
    
    def dp1(self, nums):
                  
        # i - 1    获取最大值  获取最小值
        # i        获取最大值  获取最小值
        
        dp = [[0 for i in range(2)] for j in range(len(nums))]
        dp[0][0], dp[0][1] = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            dp[i][0] = max(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1])
            dp[i][1] = min(nums[i], nums[i] * dp[i - 1][1], nums[i] * dp[i - 1][0])
        
        return max([item[0] for item in dp])
​
    
    # state compression
    def dp2(self, nums):
        
        # dp[0][0], dp[0][1] = nums[0], nums[0]
        
        res, currmax, currmin = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            currmax, currmin = max(nums[i], nums[i] * currmax, nums[i] * currmin), min(nums[i], nums[i] * currmin, nums[i] * currmax)
            
            res = max(res, currmax, currmin)
            
        return res
        
