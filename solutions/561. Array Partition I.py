class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        R = 0
        nums = sorted(nums)
        for i in range(len(nums)/2):
            R += nums[2*i]
        return R
