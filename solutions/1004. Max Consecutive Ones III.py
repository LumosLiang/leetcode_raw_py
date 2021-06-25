class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        window = collections.Counter()
        start = 0
        res = 0
        
        for end, va in enumerate(A):
            window[va] += 1
            while window[0] > K:
                window[A[start]] -= 1
                start += 1
            res = max(end - start + 1, res)
        return res
