class Trie:
​
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""
        
    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.word = word
​
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # no return, tell me start with, x, y, how many word can be found in the board
        def backtrack(x, y, node):
            
            if node.word != "":                
                res.add(node.word)
                node.word = ""
                
            if not (0 <= x < m and 0 <= y < n) or board[x][y] not in node.children:
                return 
        
            val = board[x][y]
            board[x][y] = "#"
            for i, j in [x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1]:
                backtrack(i, j, node.children[val])
​
            board[x][y] = val
            
        m, n = len(board), len(board[0])
        res = set()
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        for i in range(m):
            for j in range(n):
                backtrack(i, j, trie)
        
        return list(res)
        
​
