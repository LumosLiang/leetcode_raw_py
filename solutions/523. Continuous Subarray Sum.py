class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    
        # [23,2,4,6,7]
        
        0, 5, 1, 5, 5, 0
        # 前缀和的进一步，预处理，前缀和 + 相同余数。找相同，找相同，找相同的地方！
        
        hash = {0: -1}
        sum = 0
        
        for i, val in enumerate(nums):
            sum += val
            resid = sum % k
            if resid not in hash:
                hash[resid] = i
            else:
                if i - hash[resid] >= 2:
                    return True
                
        return False
