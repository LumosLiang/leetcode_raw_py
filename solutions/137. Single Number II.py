class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
#         2     0010
#         2     0010
#         3     0011
#         2     0010
        
        #
        res = 0
        for i in range(32):
            temp = 0
            for num in nums:
                if num >> (31 - i) & 1:
                    temp += 1
            
            if i == 0 and temp % 3:
                res = -1 << 31
            
            elif temp % 3:
                res += 1 << (31 - i) 
        
        return res
