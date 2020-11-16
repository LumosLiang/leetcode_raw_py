class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # xor
        
        res = 0
        for num in nums:
            res ^= num
        return res
            
