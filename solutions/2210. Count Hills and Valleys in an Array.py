class Solution:
    def countHillValley(self, nums: List[int]) -> int:
​
        
        res = 0
        i = 1
        
        while i < len(nums) - 1:
            
            l, r = i - 1, i + 1
            while l >= 0 and nums[l] == nums[i]: l -= 1
            while r < len(nums) and nums[r] == nums[i]: r += 1
​
            if l >= 0 and r < len(nums) and ((nums[l] < nums[i] and nums[r] < nums[i]) or (nums[l] > nums[i] and nums[r] > nums[i])):
                res += 1
                i = r
            else:
                i += 1
        
        
        return res
