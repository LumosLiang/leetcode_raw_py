class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        # trie
        
        res, l = 0, len(pref)
        
        for word in words:
            
            if len(word) >= len(pref):
                temp = True
                for j in range(l):
                    if word[j] != pref[j]:
                        temp = False
                        break
                if temp:
                    res += 1
        return res
