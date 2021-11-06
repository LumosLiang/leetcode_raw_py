class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        res = [1] * 2 * n
        fh = nums[:n]
        lh = nums[n:]
        
        for i in range(len(res)):
            if not i % 2:
                res[i] = fh.pop(0)
            else:
                res[i] = lh.pop(0)
        return res
