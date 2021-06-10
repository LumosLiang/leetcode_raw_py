class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        if target not in nums: return [-1,-1]
        
        l, r = 0, len(nums) - 1
        res = [0,0]
        
        # find the last number that n < target:
        while l <= r:
            mid = l + (r - l) // 2 
            if nums[mid] >= target: r = mid - 1
            else: l = mid + 1
        
​
        res[0] = l       
        
        l, r = 0, len(nums) - 1
        
        # find the first number that n > target:
        while l <= r:
            mid = l + (r - l) // 2 
            if nums[mid] > target: r = mid - 1
            else: l = mid + 1
        
        
        res[1] = l - 1
        return res
​
