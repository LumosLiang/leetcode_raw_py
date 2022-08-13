class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        return self.DP(s, wordDict)
        
    def sol1(self, s, wordDict):
        # backtracking       
        #     start
        #     / | 
        # cat  cats     

        res = []
        
        @lru_cache(None)
        def backtrack(idx, path):
            if idx == len(s):
                res.append(path.strip())
                return
        
            for end in range(idx + 1, len(s) + 1):
                if s[idx:end] in wordDict:
                    backtrack(end, path + s[idx:end] + " ")
        
        backtrack(0, "")
        return res
       
    def memo(self, s: str, wordDict):
        
        wordDict, l = set(wordDict), len(s)
        
        # idx, all possible paths
        memo = collections.defaultdict(list)
        memo[l] = [""]
        
        def dfs(idx):
            
            if idx not in memo:
                
                for i in range(idx + 1, l + 1):
                    temp = s[idx:i]
                    if temp in wordDict:
                        for item in dfs(i):
                            ans = (temp + " " + item).rstrip(" ")
                            memo[idx].append(ans)
                            
            return memo[idx]
            
        return dfs(0)
    
    # DP
    def DP(self, s, wordDict):
        
        # dp[i] -> s[:i] word break set
        # dp[i] = for item in dp[j] + " " + s[j: i + 1] 
        # dp[0] = [""]
        
        dp = [[]] * (len(s) + 1)
        dp[0] = [""]
        
        for i in range(1, len(s) + 1):
            dp[i] = []
            for j in range(i):
                if s[j:i] in wordDict:
                    for item in dp[j]:
                        dp[i].append(item + s[j:i] + " ")
        
        return [item.rstrip() for item in dp[-1]]
        
        
        
