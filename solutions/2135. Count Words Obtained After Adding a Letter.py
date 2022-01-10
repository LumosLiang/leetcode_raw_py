class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        res = 0
        seen = set()
        
        for word in startWords:
            seen.add("".join(sorted(word)))
        
        for word in targetWords:
            w = "".join(sorted(word))
            for i in range(len(w)):
                if w[:i] + w[i + 1:] in seen:
                    res += 1
                    break
        return res
    
    def strCompare(self, s1, s2):
#         d1 = collections.Counter(s1)
#         d2 = collections.Counter(s2)
        
#         cnt = 0
#         for key, val in d2.items():
#             if key in d1 and d1[key] == val:
#                 cnt += 1
#             if cnt == len(d2):
#                 return True
#         return False
        s1, s2 = set(s1), set(s2)
        return s1.intersection(s2) == s2
        
        
​
