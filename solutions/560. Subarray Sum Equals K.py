class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        s = 0
        hash = collections.defaultdict(int)
        hash[0] += 1
        
        res = 0
        
        for n in nums:
            s += n
            if s - k in hash:
                res += hash[s - k]
            
            hash[s] += 1
                
        return res
      
                
