class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        window, l, res = 0, 0, 0
        
        for r, val in enumerate(A):
            if not val: window += 1
            while window > K:
                if not A[l]: window -= 1
                l += 1
            
            res = max(r - l + 1, res)
        return res
