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
        
        curr = self.root
        return self._search(word, curr)
    
    def _search(self, word, start):
        
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
​
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
