class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # hash, set, addition space
        # O(N), O(N)
        
        
        # Sort()
        # O(NlogN), O(1)
        
        
        # brute force
        # O(N * N), O(1)
        
        
        # bit manipulation: XOR, move
        # O(N), O(1)
        
        res = nums[0]
        
        for i in range(1, len(nums)):
            res ^= nums[i]
        
        return res
    
        # another way
#         res = 0
        
#         for i in range(1, len(nums)):
#             res ^= nums[i]
        
#         return res
        
        
        
