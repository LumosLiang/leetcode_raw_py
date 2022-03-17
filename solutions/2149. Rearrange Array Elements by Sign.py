class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        
        pos, neg, res = [], [], [0] * len(nums)
        
        for n in nums:
            if n > 0: pos.append(n)
            if n < 0: neg.append(n)
        
        for i in range(len(pos)):
            res[i * 2] = pos[i]
            res[i * 2 + 1] = neg[i]
        
        return res
