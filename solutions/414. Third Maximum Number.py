import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            nums = [-v for v in nums]
            heapq.heapify(nums)
            for _ in range(3):
                ans = heapq.heappop(nums)
            return -ans
        
        
        
