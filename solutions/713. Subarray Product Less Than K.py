class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        l, p, res = 0, 1, 0
        
        for r, val in enumerate(nums):
            p *= val
            while l <= r and p >= k:
                p /= nums[l]
                l += 1
            res += r - l + 1
            
        return res
