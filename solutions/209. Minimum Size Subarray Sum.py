# typical sliding window problem I think.
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        total, left, right = 0, 0, 0
        min_len = float('inf')
        
        if sum(nums) < s: return 0
        
        while right < len(nums):
            total += nums[right]
            while total >= s:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
                
        return min_len
                
​
