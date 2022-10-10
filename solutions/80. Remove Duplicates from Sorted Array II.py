class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l, hash = 0, collections.Counter()
        hash[nums[0]] = 1
        
        for r in range(1, len(nums)):
            if nums[r] != nums[l] or hash[nums[l]] < 2:
                l += 1
                nums[l] = nums[r]
                hash[nums[l]] += 1
            
        return l + 1
    
    def sol1(self, nums):
        l = 0
        cnt = 1
        
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:        
                l += 1
                nums[l] = nums[r]
                cnt = 1
            elif nums[r] == nums[l] and cnt < 2:
                l += 1
                nums[l] = nums[r]
                cnt += 1
            
        return l + 1
