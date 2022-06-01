class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
#         hash
#         brute force
#         sort
#         XOR
#         Math
#         Swap sort.
        
        
        l = len(nums)
        for i in range(l):
            while nums[i] != i and nums[i] < l:
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
        
        for i in range(l):
            if i != nums[i]:
                return i
        
        return i + 1
