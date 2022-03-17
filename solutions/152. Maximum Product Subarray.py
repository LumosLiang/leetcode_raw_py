class Solution:
    def maxProduct(self, nums):
        
        # answer:
#         prev_min = prev_max = global_max = nums[0]
       
#         for num in nums[1:]:
#             minn, maxx = min(num, prev_max*num, prev_min*num), max(num, prev_max*num, prev_min*num)
#             prev_min, prev_max, global_max = minn, maxx, max(global_max, maxx)
#         return global_max
​
        # my dp, nearly correct.
#         l = len(nums)
#         curr_highest, curr_lowest, highest = nums[-1], nums[-1], nums[-1]
        
#         for i in range(l - 2, -1, -1):
#             temp = [nums[i], nums[i] * curr_highest, nums[i] * curr_lowest]
#             curr_highest, curr_lowest, highest =  max(temp), min(temp), max(max(temp), highest)
            
#         return highest
            
        # memo + backtrack
        
        l = len(nums)
        if l <= 1: return nums[0]
        
        res = float('-inf')
        memo = {}
        
        def multp(nums, start, end):
            
            if start == end: return nums[start]
            
            res = 1
            for i in range(start, end + 1):
                res *= nums[i]
    
            return res
​
        for i in range(l):
            for j in range(i, l):
                tk = str(i) + str(j)
                if tk in memo:
                    res = max(res, memo[tk])
                else:
                    tv = multp(nums, i, j)
                    memo[tk] = tv
                    res = max(res, tv)
        return res
                 
                
                
        
                
                
                
        
        
