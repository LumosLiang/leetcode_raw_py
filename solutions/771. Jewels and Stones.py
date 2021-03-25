class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
       
    
        setJ = set(J)
        return sum(s in setJ for s in S)
