class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
    
        if len(nums) % k != 0: return False
        
        cnt, res = 0, len(nums) // k
    
        d = dict(sorted((collections.Counter(nums)).items()))
        
        while d:
            m = next(iter(d))
            for _ in range(k):
                if m in d:
                    d[m] -= 1
                    if d[m] == 0:
                        del d[m]
                else:
                    return False
                m += 1
            cnt += 1
        
        return cnt == res
        
