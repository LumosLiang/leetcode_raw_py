class Solution:
    def matrixReshape(self, nums, r, c):
        if len(nums) * len(nums[0]) != r * c:
            return nums
​
        res = [[0] * c for _ in range(r)]
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                i_update = (i * len(nums[0]) + j) // c
                j_update = (i * len(nums[0]) + j) % c
                res[i_update][j_update] = nums[i][j]
        
        return res
