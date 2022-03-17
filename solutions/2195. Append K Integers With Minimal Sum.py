class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        res = 0
        nums.sort()
        nums = [0] + nums + [float('inf')]
        
        for i in range(1, len(nums)):
            diff = min(nums[i] - nums[i - 1] - 1, k)
            if diff > 0:
                res += (nums[i - 1] + 1 + nums[i - 1] + diff) * diff // 2
                k -= diff
                if k == 0:
                    break
​
        return res
                
            
        
        
        
