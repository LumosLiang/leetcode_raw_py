class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
        # 先归到一个确定的区间内。
        
        # [2,2,5,0,2,2,2,2,2], 0
        
        # 方案1：先去掉，但是更改原队列感觉不太好
        # while len(nums) > 1 and nums[-1] == nums[0]: nums.pop()
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            # 方案2：和方案1差不多，但是移动left去除元素（移动right 也行）
            
            while l + 1 < r and nums[l] == nums[l + 1]:
                l += 1
            
            mid = (l + r) // 2
            
            # 归区间
            if nums[mid] > nums[r] and target <= nums[r]:
                l = mid + 1
            elif nums[mid] <= nums[r] and target > nums[r]:
                r = mid - 1
            # 做二分
            else:
                if nums[mid] >= target:
                    r = mid
                elif nums[mid] < target:
                    l = mid + 1
        
        return nums[l] == target
    
