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
    
​
    def sol2(self, nums: List[int], target: int):
        nums.sort()
        diff = float('inf')
        res = float('inf')
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            new_target = target - nums[i]
            curr = nums[l] + nums[r]
            
            while l < r:
                s = nums[l] + nums[r]
                
                if abs(s - new_target) < abs(curr - target):
                    curr = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    break
            
            temp = abs(curr + nums[i] - target)
            if temp < diff:
                res = 
        
        return res
