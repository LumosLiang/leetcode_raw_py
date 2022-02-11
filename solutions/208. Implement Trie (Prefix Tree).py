​
class TrieNode:
    def __init__(self):
        self.list = [None] * 26
        self.IsEndChar = False
​
class Trie:
​
    def __init__(self):
        self.root = TrieNode()
​
    def insert(self, word: str) -> None:
        curr = self.root
        
        for chr in word:
            idx = ord(chr) - ord('a')
            if not curr.list[idx]:
                curr.list[idx] = TrieNode()
            curr = curr.list[idx]
        
        curr.IsEndChar = True
​
    def search(self, word: str) -> bool:
        
        curr = self.root
        for chr in word:
            idx = ord(chr) - ord('a')
            if not curr.list[idx]:
                return False
            curr = curr.list[idx]
        
        return curr.IsEndChar
​
    def startsWith(self, prefix: str) -> bool:
​
        curr = self.root
        for chr in prefix:
            idx = ord(chr) - ord('a')
            if not curr.list[idx]:
                return False
            curr = curr.list[idx]
        
        return True
​
    # Dic Way
class TrieNode:
    def __init__(self, isEndNode = False):
        self.dict = {}
        self.isEndNode = isEndNode
​
class Trie:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
​
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for w in word:
            if w not in curr.dict:
                curr.dict[w] = TrieNode()
            curr = curr.dict[w]
        curr.isEndNode = True
