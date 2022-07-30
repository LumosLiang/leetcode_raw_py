class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # sort, hash
        # bit
        bit = [0] * 32
        
        for num in nums:
            for i in range(32):
                if num >> i & 1:
                    bit[31 - i] += 1
        
        for i in range(32):
            if bit[i] % 3:
                bit[i] = 1
            else:
                bit[i] = 0
        
        ans = 0
        if bit[0]: ans = -1 << 31
        for i in range(1, 32):
            ans += bit[i] * 1 << (31 - i)
            
        return ans
