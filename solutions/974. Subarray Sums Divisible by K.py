class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
#         prefix
#         [4,5,0,-2,-3,1]
#        0,4,9,9,7,4,5
#        0,4,4,4,3,4,0
        
#         x % k = (x + k * m) % k = x % k + 0
        
    # 1. prefix + 相同余数
    # 2. 算个数 还是算长度
    
        presum = 0
        hash = collections.Counter()
        hash[0] = 1
        res = 0
        
        for num in nums:
            presum += num
            resid = presum % k
            if resid in hash:
                res += hash[resid]
            hash[resid] += 1
        
        return res
        
