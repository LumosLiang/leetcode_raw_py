class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.sol1(nums, target)
    
    # typical O(logN), O(1)
    def sol1(self, nums: List[int], target: int):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            temp = nums[mid]
            if temp == target: return mid
            elif temp > target: r = mid - 1
            else: l = mid + 1
        
        return -1
        
    # another way O(logN), O(1)
    def sol2(self, nums: List[int], target: int):
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            temp = nums[mid]
            
            if temp >= target: r = mid
            else: l = mid + 1
        
        return l if nums[l] == target else -1
