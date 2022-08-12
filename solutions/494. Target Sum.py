class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
  #       +                   -
  #    +     -              +   -
  # +   -   +   -
        memo = {}
        def dfs(idx, ex_sum):
            nonlocal memo
​
            if idx == len(nums):
                return 1 if not ex_sum else 0
            
            if (idx, ex_sum) not in memo: 
                temp = dfs(idx + 1, ex_sum - nums[idx]) + dfs(idx + 1, ex_sum + nums[idx])
                memo[(idx, ex_sum)] = temp
        
            return memo[(idx, ex_sum)]
        
        return dfs(0, target)
        
        # typical backtrack
        # why not bfs? Because it is the path here matters
#         start
#          / \
#         +   -
#        / \  / \
#       +  -  +  -
#          ....
​
#         res = 0
        
#         # DFS
#         def dfs(idx, ex_sum):
#             nonlocal res
           
#             if idx == len(nums):
#                 if ex_sum == S:
#                     res += 1
#                 return
            
#             for sign in [0, 1]:
#                 if sign:
#                     dfs(idx + 1, ex_sum + nums[idx])
#                 else:
#                     dfs(idx + 1, ex_sum - nums[idx])
                    
#         dfs(0, 0)
        
#         return res
​
#         memo = {}
        
#         # dfs 是在idx处，有多少种表达式可以表达 ex_sum
#         def dfs(idx, ex_sum):
#             nonlocal memo
​
#             if idx == len(nums):
#                 return 1 if not ex_sum else 0
            
#             if (idx, ex_sum) not in memo: 
#                 temp = dfs(idx + 1, ex_sum - nums[idx]) + dfs(idx + 1, ex_sum + nums[idx])
#                 memo[(idx, ex_sum)] = temp
        
#             return memo[(idx, ex_sum)]
        
#         return dfs(0, S)
    
#         # DP
#         i = 0: -1, 1
#         nums[i+1:] target + 1, target -1
#         dp[i] nums[i:] 有多少way == targetsum
#         dp[i - 1] 有多少way == targetsum - nums[i + 1], targetsum + nums[i - 1]
