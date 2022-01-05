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
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.dict:
                return False
            # if word[i] in curr.dict:
            curr = curr.dict[prefix[i]]
        
        return True
