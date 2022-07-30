class Solution:
    def reverseBits(self, n: int) -> int:
        # 取bit 然后算
        res = 0
        for i in range(31, -1, -1):
            temp = n >> i & 1
            res += temp * (1 << (31 - i))
        
        return res 
