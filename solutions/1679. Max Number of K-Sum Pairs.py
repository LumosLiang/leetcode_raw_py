class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        hash = {}
        
        for n in nums:
            if n in hash and hash[n] == 1: 
                count += 1
                hash[n] += 1
            else: 
                hash[k - n] = 1
        
        return count
                
