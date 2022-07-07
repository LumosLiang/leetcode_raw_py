class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        return self.DP(nums)
    
    # 先想清楚，我有选择。所以DFS可以做，结果TLE
    def DFS(self, nums):
        self.res = 0
        
        def backtrack(choices, money):
            
            if not choices:
                self.res = max(self.res, money)
                return
        
            for i in range(len(choices)):
                backtrack(choices[:i] + choices[i + 1:], money + (choices[i - 1] if i - 1 >= 0 else 1) * choices[i] * (choices[i + 1] if i + 1 < len(choices) else 1))
        
        backtrack(nums, 0)
                
        return self.res
​
    # 如果想优化这个过程，就是直接要有return，
    
    def DP(self, nums):
    
        nums = [1] + nums + [1]
        
        @lru_cache(None)
        def backtrack(left, right):
            if left > right: return 0
​
            temp = 0
            for i in range(left, right + 1):
                temp = max(temp, backtrack(left, i - 1) + nums[left - 1] * nums[i] * nums[right + 1] + backtrack(i + 1, right))
            return temp
        
        return backtrack(1, len(nums) - 2)
    
​
        
