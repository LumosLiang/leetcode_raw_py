class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
         
        nums.sort()
        n = len(nums)
        res = {}
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            new_targ = target - nums[i]
            
            l, r = i + 1, n - 1
            min_diff = float('inf')
            temp = [0] * 2
            
            while l < r:
                s = nums[l] + nums[r]
                d = abs(s - new_targ)
                
                if s < new_targ:
                    if d < min_diff:
                        min_diff = d
                        temp[0] = nums[l]
                        temp[1] = nums[r]
                    l += 1
                elif s > new_targ:
                    if d < min_diff:
                        min_diff = d
                        temp[0] = nums[l]
                        temp[1] = nums[r]
                    r -= 1
                else:
                    temp[0] = nums[l]
                    temp[1] = nums[r]
                    break
                
            s = nums[i] + sum(temp)
            res[abs(target - s)] = s
        
        return res[min(res)]
                
                
                
                
        
