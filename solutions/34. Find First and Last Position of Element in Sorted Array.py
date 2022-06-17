class Solution:
    def searchRange(self, nums, target):
        return self.sol2(nums, target)
    
    def sol1(self, nums, target):
        
        # search the first equal one
        def search_left(target):
            lo, hi = 0, len(nums) - 1
            
            while lo < hi:
                mid = (lo + hi) // 2
                
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            
            return lo if nums and nums[lo] == target else -1
        
        # 注意的细节：1. 左中点，2， 搜第一个大的数，那么搜索区间要注意。3，逼近方向和中点选择
        def search_right(target):
            lo, hi = 0, len(nums)
            
            while lo < hi:
                mid = (lo + hi) // 2
                
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            
            return lo - 1 if nums and nums[lo - 1] == target else -1
        
        # 注意的细节：1. 右中点，2， 搜最后一个相等的数，搜索区间要注意。3，逼近方向和中点选择
        def search_right2(target):
            lo, hi = 0, len(nums) - 1
            
            while lo < hi:
                mid = (lo + hi) // 2 + 1
                
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid
            
            return lo if nums and nums[lo] == target else -1
        
        return [search_left(target), search_right2(target)]
    
    # 这个方法更简洁一点
    # 只写一个方法：找第一个相等的数的idx，如果不存在，返回第一个比它大的数
    # 先找左边界，找到以后，再找右边界，但是不需要重新写，
    def sol2(self, nums, target):
        
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]
