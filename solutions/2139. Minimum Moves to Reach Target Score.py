class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        res = 0
        
        while target > 1:
            
            if maxDoubles > 0:
                curr = target // 2
                resid = target - curr * 2
                res += resid + 1
                maxDoubles -= 1
            else:
                break
                
            target = curr
            
        res += target - 1
        
        return res
