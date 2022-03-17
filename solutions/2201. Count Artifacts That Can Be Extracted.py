class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        
        res = 0
        
        isdig = [[False for i in range(n)] for j in range(n)]
        
        for d in dig:
            x, y = d[0], d[1]
            isdig[x][y] = True
           
        
        for af in artifacts:
            
            x1, y1 = af[0], af[1]
            x2, y2 = af[2], af[3]
            
            temp = True
            
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if not isdig[i][j]:
                        temp = False
                        break
​
            res += (1 if temp else 0)
                
        return res
