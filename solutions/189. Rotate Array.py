class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        while k != 0:
            nums.insert(0, nums[-1])
            nums.pop(-1)
            k -= 1
        
