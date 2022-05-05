class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # binary search
        
        l, r = 0, len(nums) - 1
        
        # 这里还是归区间的逻辑
        # 但是答案逐渐收敛到不断的进行归区间之中
        
        while l < r:
            mid = (l + r) // 2
    
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid    
            
        return nums[l]
    
​
    
    
