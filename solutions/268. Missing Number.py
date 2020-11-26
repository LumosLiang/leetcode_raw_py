class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0
        for i in nums:
            res ^= i
​
        for i in [j for j in range(len(nums)+1)]:
            res ^= i
            
        return res
            
