class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return self.sol2(nums, target)
    
    def sol1(self, nums: List[int], target: int):
        nums.sort()
        res = float('inf')
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
           
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return res
        
        return res
    
    # follow-up, tell me the closest, if there are multiple, record them all.
    def sol2(self, nums: List[int], target: int):
        nums.sort()
        threesum = float('inf')
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
        
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                
                if abs(s - target) < abs(threesum - target):
                    threesum = s
                    res = [nums[l], nums[r], nums[i]]
                    
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    break
            
        return res
