class Solution:
    def findDuplicates(self, nums):
        
        res = set()
        
        for i in range(len(nums)):
            while nums[i] != i + 1:
                temp = nums[i]
                nums[i], nums[temp - 1] = nums[temp - 1], nums[i]
                if nums[i] == nums[nums[i] - 1] and i != nums[i] - 1:
                    res.add(nums[i])
                    break
        return list(res)
​
    
