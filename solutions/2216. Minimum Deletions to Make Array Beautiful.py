class Solution:
    def minDeletion(self, nums: List[int]) -> int:
       
​
        res = 0
             
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            res += (j - i - 1 if j < len(nums) else j - i)
            i = j + 1
            
        return res
