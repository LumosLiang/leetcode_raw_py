import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        
        while start <= end:
            mid = start + (end - start) // 2
            
            temp = 0
            for n in nums:
                temp += math.ceil(n / mid)
            if temp <= threshold: end = mid - 1 
            else: start = mid + 1
                
        return start
