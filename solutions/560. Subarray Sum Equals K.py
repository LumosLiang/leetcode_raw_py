class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = [0] * (len(nums) + 1) 
        
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
            
        hash = collections.Counter()
        
        res = 0
        for val in prefix:
            if val in hash:
                res += hash[val]        
            hash[val + k] += 1
            
        return res
            
            
                
        
        
