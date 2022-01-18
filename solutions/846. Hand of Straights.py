class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
   
        if len(hand) % groupSize != 0: return False
        
        cnt, res = 0, len(hand) // groupSize
    
        d = dict(sorted((collections.Counter(hand)).items()))
        
        while d:
            m = next(iter(d))
            for _ in range(groupSize):
                if m in d:
                    d[m] -= 1
                    if d[m] == 0:
                        del d[m]
                else:
                    return False
                m += 1
            cnt += 1
        
        return cnt == res
        
