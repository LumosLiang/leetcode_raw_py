class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # [1,3,6,2,1,6]
        # [3,4,5,1,4,2]
        
        # insights
        # 每一步的最优解就是最后的解
        # 1. must start from diff > 0
        # 2. if face any runsum < 0, then any station include and behind this station are excluded
        
        
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        # diff += diff
        length = len(gas)
        
        rsum = 0
        l = 0
        
        for r in range(length * 2):
            rsum += diff[r % length]
            
            if rsum < 0: 
                l = r + 1
                rsum = 0
            
            if r - l + 1 == length:
                return l
            
        return -1
        
