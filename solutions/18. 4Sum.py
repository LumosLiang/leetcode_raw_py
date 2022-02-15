​
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # return self.solution1(nums, target)
        return self.solution2(nums, target)
    
    # TLE int
    def solution1(self, nums, target):↔​
        
    # two pointers 
        # not sorted - two sum - hashmap - O(N)
        # sort - two sum - two pointer - O(NlogN) + O(N)
        # sort - three sum -  O((N - 2) * N)
        # sort - four sum - O((N - 3) * ((N - 2) * N))
    
    def solution2(self, nums, target):
        if len(nums) < 4: return None
        
        nums.sort()
        res, l = [], len(nums)
        
        for i in range(l - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            target_three = target - nums[i]
            
            for j in range(i + 1, l - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                target_two = target_three - nums[j]
                
                p1, p2 = j + 1, l - 1
                
                while p1 < p2:
                    if nums[p1] + nums[p2] == target_two:
                        res.append([nums[i], nums[j], nums[p1], nums[p2]])
                        while p1 < p2 and nums[p1 + 1] == nums[p1]: p1 += 1
                        while p1 < p2 and nums[p2 - 1] == nums[p2]: p2 -= 1
                        p1 += 1
                        p2 -= 1
                    elif nums[p1] + nums[p2] > target_two:
                        p2 -= 1
                    else:
                        p1 += 1
        
        return res
                
                
                
                
                
                
            
        
        
        
        
