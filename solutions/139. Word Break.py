            if w not in curr.dict:
                curr.dict[w] = TrieNode()
            curr = curr.dict[w]
        curr.isEndNode = True
​
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.dict:
                return False
            curr = curr.dict[word[i]]
        return curr.isEndNode
​
​
class Solution:
    
    # DP + Trie
    def wordBreak(self, s: str, wordDict) -> bool:
        
        l = len(s)
        dp = [None] * (l + 1)
        dp[-1] = True
        
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        for i in range(len(s) - 1, -1, -1):
            temp = False
            for j in range(i + 1, len(s) + 1):
                if trie.search(s[i:j]) and dp[j]:
                    temp = True
                    break
            dp[i] = temp
 
        return dp[0]
    
    #  backtrack 
    def wordBreakBT(self, s: str, wordDict) -> bool:
        
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
                if i not in visited and s[node:i] in wordDict:
                    if i == len(s):
                        return True
                    visited.add(i)
                    q.append(i)
        return False
 
    
    # DP bottom-up
​
    def wordBreakDP(self, s: str, wordDict) -> bool:
        
        l = len(s)
        dp = [None] * (l + 1)
        dp[-1] = True
        
        for i in range(len(s) - 1, -1, -1):
            temp = False
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict and dp[j]:
                    temp = True
                    break
            dp[i] = temp
 
        return dp[0]
​
