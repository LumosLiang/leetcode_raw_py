class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atMost(k):
            start, res = 0, 0
            
            for end, val in enumerate(nums):
                if val % 2: k -= 1
                    
                while k < 0:
                    if nums[start] % 2:k += 1
                    start += 1
                res += end - start + 1
            
            return res
        
        return atMost(k) - atMost(k - 1)
        
        
        
        
