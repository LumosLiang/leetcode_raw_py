class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        
        # prefix-sum
        
        for i in range(len(nums)):
            if i > 0:
                nums[i] += nums[i - 1]
        
        dit = {}
        m = float('-inf')
        
        for i in range(len(nums) + 1):
            if i == 0:
                score_i = nums[-1]
            else:
                score_i = i - nums[i - 1] + nums[-1] - nums[i - 1]
                
            if score_i not in dit:
                dit[score_i] = [i]
            else:
                dit[score_i].append(i)
            
            m = max(m, score_i)
            
        return dit[m]
            
