class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count, left, right = 0, 0, len(nums) - 1
        nums.sort()
        
        while left < right:
            s = nums[left] + nums[right]
            if s == k:
                count += 1
                left += 1
                right -= 1
            elif s < k:
                left += 1
            else:
                right -= 1
        return count
                
