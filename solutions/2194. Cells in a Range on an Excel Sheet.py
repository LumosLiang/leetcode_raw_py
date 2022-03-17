class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        coords = s.split(":")
        start, end = coords[0], coords[1]
        
        res = []
        
        
        for i in range(ord(start[0]), ord(end[0]) + 1):
            for j in range(ord(start[1]), ord(end[1]) + 1):
                res.append(chr(i) + chr(j))
        
        return res
                
