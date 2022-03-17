class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
 
        nums.sort()
        
        while self.binaryS(nums, original):
            
            original = 2 * original
        
        return original
        
        
    def binaryS(self, nums, target):
        
        l, r =  0, len(nums) - 1
        
        while l <= r:
            
            mid = l + (r - l) // 2
            if nums[mid] == target: return True
            elif nums[mid] < target: l = mid + 1
            else: r = mid - 1 
                
        return False
            
            
        
        
        
