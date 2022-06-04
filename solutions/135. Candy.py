class Solution:
    def candy(self, ratings: List[int]) -> int:
        
#         afterward
        
#         1. if curr > pre: candy[pre] + 1
#         2. if curr <= pre: 1
        
#         backward
        
#         3. if curr > pre: candy[pre] + 1
        
        return self.sol2(ratings)
    
    def sol1(self, ratings):
        
        l = len(ratings)
        res = [1] * l
        
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        
        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
                res[i] = res[i + 1] + 1
                
        return sum(res)
        
    # dp + memo
    
    def sol2(self, ratings):
        
        l = len(ratings)
        dp = [0] * l
        res = 0
        
        # give me the least candy that assgin to index i child.
        def dfs(i):
            nonlocal ratings
            
            if dp[i] <= 0:
                
                left = 0
                if i > 0 and ratings[i] > ratings[i - 1]:
                    left = dfs(i - 1)
​
                right = 0
                if i < l - 1 and ratings[i] > ratings[i + 1]:
                    right = dfs(i + 1)
​
                dp[i] = max(left, right) + 1
                
            return dp[i]
        
        for i in range(l):
            res += dfs(i)
        
        return res
​
    
