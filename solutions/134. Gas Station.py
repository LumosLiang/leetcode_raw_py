class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
         
        length = len(gas)
        diff = [gas[i] - cost[i] for i in range(length)]
        
        diff += diff
        
        l, r = 0, 0 
        
        while r < 2 * length:
            
            if diff[r] >= 0:
                temp, cnt = 0, 0
                
                while r < 2 * length and temp + diff[r] >= 0:
                    temp += diff[r]
                    cnt += 1
                    if cnt == length:
                        return l
                    r += 1
            r += 1
            l = r
        
        return -1
    
         
