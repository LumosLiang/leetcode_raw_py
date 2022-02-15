# shrink boundary
​
class Solution:
    
    # clearer
    def findMin1(self, nums: List[int]) -> int:
        
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            elif nums[mid] < nums[0]:
                r = mid - 1
            elif nums[mid] > nums[-1]:
                l = mid + 1
    
    # Best one
    def findMin(self, nums: List[int]) -> int:
        
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            
            mid = (l + r) // 2 
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
                
                
            
            
                    
             
            
            
            
            
            
