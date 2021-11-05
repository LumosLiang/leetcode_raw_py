class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for i in range(len(nums)):
            if nums[i] in hash:
                return [i, hash[nums[i]]]
            else:
                hash[target - nums[i]] = i
