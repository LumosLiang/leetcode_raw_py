class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        
        if len(nums) == 1: return nums
        
        res = []
        
        nums.sort()
        
        for i in range(len(nums)):
            if i == 0:
                if nums[i] != nums[i + 1] and nums[i + 1] != nums[i] + 1:
                    res.append(nums[i])                
            elif i == len(nums) - 1:
                if nums[i] != nums[i - 1] and nums[i - 1] != nums[i] - 1:
                    res.append(nums[i]) 
            else:
                temp = [nums[i] - 1, nums[i] + 1, nums[i]]
                if nums[i - 1] not in temp and nums[i + 1] not in temp:
                    res.append(nums[i])
        
        return res
