class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return self.solution2(nums)
    
    # O(N)
    def solution1(self, nums):
        # sliding window
        
        res, l, r = 0, 0, 0
        
        while r < len(nums):
            if nums[r] == 1:
                while r < len(nums) - 1 and nums[r + 1] == nums[r]:
                    r += 1
                res = max(res, r - l + 1)
            
            r += 1
            l = r 
                
        return res
        
    # prefix sum O(2 * N)
    def solution2(self, nums: List[int]) -> int:
        
        res, last = 0, 0
        
        nums.append(0)
        
        for i in range(len(nums)):
            if i != 0:
                nums[i] += nums[i - 1]
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                res = max(res, nums[i] - last)
                last = nums[i]
        
        return res
