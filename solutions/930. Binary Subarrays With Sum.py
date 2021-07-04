class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def numSubarraysWithinSum(goal):
            if goal < 0: return 0
            start, res = 0, 0
​
            for end, val in enumerate(nums):
                goal -= val
                while goal < 0:
                    goal += nums[start]
                    start += 1
                res += end - start + 1
            return res
        return numSubarraysWithinSum(goal) - numSubarraysWithinSum(goal - 1)
    
​
