class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = {}
        
        for r, val in enumerate(nums):
            
            if val in window and r - window[val] <= k:
                return True
                
            window[val] = r
                
        return False
