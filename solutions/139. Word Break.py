class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        return self.sol2(s, wordDict)
    
    # backtrack + LRU 
    def sol1(self, s: str, wordDict):
        self.res = False
        
        @lru_cache(None)
        def backtrack(word, path):
            
            if not word:
                self.res = True
                return
            
            for i in range(len(word)):
                if word[:i + 1] in wordDict:
                    backtrack(word[i + 1:], path + word[:i + 1])
            
        backtrack(s, "")
            
        return self.res
    
    # backtrack + memo
    def sol2(self, s: str, wordDict):
        
        memo = {} 
        wordDict = set(wordDict)
    
        # if the word s[idx:] can be break against wordDict
        def backtrack(idx):
            nonlocal s
            nonlocal wordDict
            
            if idx not in memo:
                memo[idx] = False
                
                if idx == len(s):
                    memo[idx] = True
                
                else:
                    for i in range(idx + 1, len(s) + 1):
                        if s[idx:i] in wordDict and backtrack(i):
                            memo[idx] = True
                            break
            return memo[idx]
        
        return backtrack(0)
    
    # dp
    def sol3(self, s: str, wordDict):
    
        # state: dp[i] 是s[i:]是否可以满足条件
        # base: dp[-1] = True
        # dp[i] = any[if s[i:i + len(word)] match and dp[i + len(word)]]
        
        # bottom up DP
        
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        
        for i in range(len(s) - 1, -1, -1):
            
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict and dp[j]:
                    dp[i] = True
                    break    
            
        return dp[0]
    
    # another dp, but more like BFS
    def sol4(self, s: str, wordDict):

        visited = set()
        q = collections.deque([len(s) - 1])
        visited.add(len(s) - 1)
        wordDict = set(wordDict)
        
        while q:
            curr_idx = q.pop()
            
            for i in range(curr_idx, -1, -1):
                if i not in visited and s[i:curr_idx + 1] in wordDict:
                    if i == 0:
                        return True
                    visited.add(i)
                    q.append(i)
        return False
