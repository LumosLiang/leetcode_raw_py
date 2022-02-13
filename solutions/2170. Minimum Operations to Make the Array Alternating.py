class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return 0
        
        # to fit in [A,B,A,B,A,B,A,B]
        
        ditA = collections.Counter()
        ditB = collections.Counter([nums[2 * i + 1] for i in range(len(nums) // 2 )])
        
        if len(nums) % 2:
            ditA = collections.Counter([nums[2 * i] for i in range(len(nums) // 2 + 1)])
        else:
            ditA = collections.Counter([nums[2 * i] for i in range(len(nums) // 2)])
            
        maxA, maxB = ditA.most_common(2), ditB.most_common(2)
        
        
        # compute res
        res = 0
        
        if maxA[0][0] == maxB[0][0]:
            
            
            temp1 = - maxA[0][1] + (len(nums) // 2 + 1 if len(nums) % 2 else len(nums) // 2 ) +  (len(nums) // 2 if len(maxB) == 1 else len(nums) // 2  - maxB[1][1]) 
            temp2 = (- maxA[1][1] if len(maxA) > 1 else 0) + (len(nums) // 2 + 1 if len(nums) % 2 else len(nums) // 2 ) +  (len(nums) // 2 - maxB[0][1])
            
            res = min(temp1, temp2)
        else:
            res = - maxA[0][1] + (len(nums) // 2 + 1 if len(nums) % 2 else len(nums) // 2 ) +  (len(nums) // 2 - maxB[0][1])
            
        return res
            
            
            
