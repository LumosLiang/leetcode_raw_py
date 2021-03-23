import collections
class Solution:
    def twoSum(self, nums, target):
        dit = {}
        for k,v in enumerate(nums):
            dit[v] = k
        dit = collections.OrderedDict(sorted(dit.items()))
        nums.sort()
        
        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [dit[nums[l]], dit[nums[r]]]
            elif s < target:
                l += 1
            else:
                r -= 1
        
        return None
​
