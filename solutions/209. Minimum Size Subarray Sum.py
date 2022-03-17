# typical sliding window problem I think.
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # O(N), O(1)
        
        sum, l, res = 0, 0, len(nums) + 1
        
        for r, val in enumerate(nums):
            sum += val
            while sum >= s:
                res = min(res, r - l + 1)
                sum -= nums[l]
                l += 1
      
        return res if res != len(nums) + 1 else 0
            
        
                
​
