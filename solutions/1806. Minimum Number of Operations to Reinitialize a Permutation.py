class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
        res = 0
        init, perm = list(range(n)), list(range(n))
        
        while res == 0 or perm != init:
            perm = [perm[int(i / 2)] if i % 2 == 0 else perm[int(n / 2 + int(i - 1) / 2)] for i in range(n)]
            res += 1
​
        return res
​
