# backtrack + memo, essentially DFS
​
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        
        self.dict = {}
        wordDict = set(wordDict)
        
        def backtrack(word, idx):
            
            if idx == len(word):
                return True
            
            if idx in self.dict:
                return self.dict[idx]
            
            for i in range(idx + 1, len(word) + 1):
                if word[idx:i] in wordDict:
                    res = backtrack(word, i)
                    
                    if res:
                        return True
                    else:
                        self.dict[i] = False
            return False
​
        return backtrack(s, 0)
        
# BFS, think about it as a Graph, there are vertices and edges
​
    def wordBreakBFS(self, s: str, wordDict) -> bool:
        
        visited = set()
        q = collections.deque([0])
        visited.add(0)
        wordDict = set(wordDict)
        
        while q:
            node = q.pop()
            
            for i in range(node + 1, len(s) + 1):
                if i not in visited:
                    if s[node:i] in wordDict:
                        if i == len(s):
                            return True
                        visited.add(i)
                        q.append(i)
        return False
 
    
# DP
        
# Trie
