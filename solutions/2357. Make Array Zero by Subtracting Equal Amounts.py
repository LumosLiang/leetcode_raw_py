class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        res, l = 0, len(nums)
        
        while sum(nums):
            
            temp = min([num for num in nums if num])
            
            for i in range(l):
                if nums[i]:
                    nums[i] -= temp
            res += 1
            
        return res
