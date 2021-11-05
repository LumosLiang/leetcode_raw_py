class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1: return nums[0]        
        return max(self.rob_helper(nums[:l - 1]), self.rob_helper(nums[1:]))
        
        
    def rob_helper(self, nums):
         
        pre, prepre, curr = 0, 0, 0
        
        for i in range(len(nums)):
            curr = max(pre, prepre + nums[i])
            prepre = pre
            pre = curr
        
        return curr
        
