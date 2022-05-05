class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        # [6,7,0,1,2,3,4,5]
        # [3,4,5,6,7,0,1,2]
        # decide which part mid locate
        # decide which part target locate
        
        # 先归到一个确定的区间内。
        
        while l <= r:
            mid = (l + r) // 2
            
            # for 更快
            if nums[mid] == target: return mid
            
            # 归区间
            if nums[mid] > nums[r] and target <= nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r] and target > nums[r]:
                r = mid - 1
            else:
                # 做二分
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1
    
    
