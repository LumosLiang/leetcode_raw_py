class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # hash 
        res = []
        for k,v in collections.Counter((A + " " + B).split()).items():
            if v == 1:
                res.append(k)
        return res
