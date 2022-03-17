class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        if len(nums) < 3: return 0
        
        nums.sort()
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            while l < len(nums) -1 and nums[l] == nums[l + 1]: l += 1
            while r > 0 and nums[r] == nums[r - 1]: r -= 1
            
            if l <= r:break
        
        res = r - l - 1
        return res if res > 0 else 0 
        
