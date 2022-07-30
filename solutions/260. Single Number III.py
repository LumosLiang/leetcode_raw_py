class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        # 分组异或的思想
        
        diff = 0
        for num in nums:
            diff ^= num
        
        diff = diff & (-diff)
        
        res = [0, 0]
        for num in nums:
            if num & diff:
                res[0] ^= num
            else:
                res[1] ^= num
                
        return res
