# hash
import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        hash = collections.Counter(nums)
        res = []
        for k,v in hash.items():
            if v == 1:
                res.append(k)
        
        return res
        
        
        
