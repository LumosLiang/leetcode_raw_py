class TrieNode:
    def __init__(self, isEndChar = False):
        self.dict = {}
        self.isEndChar = isEndChar
​
class WordDictionary:
​
    def __init__(self):
        self.root = TrieNode()
​
    def addWord(self, word: str) -> None:
        
        curr = self.root
        for w in word:
            if w not in curr.dict:
                curr.dict[w] = TrieNode()
            curr = curr.dict[w]
        curr.isEndChar = True
​
    def search(self, word: str) -> bool:
        
#         return self._search(word, self.root)
        
        self.res = False
        self.DFS(word, 0, self.root)
        return self.res
    
    def _search(self, word, start):
​
        curr = start
        for i in range(len(word)):
  
            if word[i] == ".":
                if not curr.dict: return False
                return any([self._search(word[i + 1:], curr.dict[key]) for key in curr.dict])
                 
            if word[i] not in curr.dict: 
                return False
            
            curr = curr.dict[word[i]]
        
        return curr.isEndChar
​
    def DFS(self, word, idx, node):
        
        if idx == len(word):
            if node.isEndChar:
                self.res = True
            return
        
        if word[idx] in node.dict:
            self.DFS(word, idx + 1, node.dict[word[idx]])
            
        if word[idx] == ".":
            for value in node.dict.values():
                self.DFS(word, idx + 1, value)
            
