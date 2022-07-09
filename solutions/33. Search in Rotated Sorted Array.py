class Solution:
    def search(self, nums, target):
    
        return self.sol2(nums, target)
    
    def sol1(self, nums):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target: return mid
            
            if nums[mid] > target:
                if target >= nums[0] or nums[mid] <= nums[-1]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target <= nums[-1] or nums[mid] >= nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1
    
        return -1
​
    def sol2(self, nums, target):
        # 先归区间，再做二分
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            
            mid = l + (r - l) // 2
            
            if nums[mid] == target: return mid
            
            if nums[mid] > nums[r] and target <= nums[r]:
                l = mid + 1
            elif nums[mid] <= nums[r] and target > nums[r]:
                r = mid - 1
            else:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
        
        return l if nums[l] == target else -1
                        
            
