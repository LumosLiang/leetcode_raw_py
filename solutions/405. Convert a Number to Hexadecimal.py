class Solution:
    def toHex(self, num: int) -> str:
        
        # best way is to convert to 32 bit binary and take 4 by 4 each time
        
        if not num: return "0"
        
        hash = "0123456789abcdef"
        
        res = ""
        
        for i in range(7, -1, -1):
            binary_part = (num >> (4 * i)) & 0xf
            res += hash[binary_part]
        
        return res.lstrip("0")
