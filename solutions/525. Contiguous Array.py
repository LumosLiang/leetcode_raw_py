class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
​
#         [0, 1, 0, 1, 0, 0, 1]       
#       0, -1, 0, -1, 0, -1, -2, -1
​
        l = len(nums)
        prefix = [0] * (l + 1)
        for i in range(l):
            if nums[i] == 1:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i] - 1
        
        hash = {}
        res = 0
        for i, val in enumerate(prefix):
            if val not in hash:
                hash[val] = i
            else:
                res = max(res, i - hash[val])
        return res
            
        
