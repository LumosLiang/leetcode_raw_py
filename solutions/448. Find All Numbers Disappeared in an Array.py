class Solution:
    def findDisappearedNumbers(self, nums):
        standard_lst = [i for i in range(1, len(nums) + 1)]
        return list(set(standard_lst).difference(set(nums)))
        
