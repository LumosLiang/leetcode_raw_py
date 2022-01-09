class Solution:
    def minSwaps(self, nums: List[int]) -> int:
​
        cntone = 0
        
        for n in nums:
            if n == 1:
                cntone += 1
    
        l, res = 0, float('inf')
        nums.extend(nums)
        
        need = {0:0, 1:0}
        for r, val in enumerate(nums):
            need[val] += 1
                
            if need[0] + need[1] == cntone:
                res = min(res, need[0])
                need[nums[l]] -= 1
                l += 1
                
        return res if res != float('inf') else 0
            
