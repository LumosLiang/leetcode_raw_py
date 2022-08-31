class Solution:
    def toHex(self, num: int) -> str:
        
        # 16 + 8 + 2
        # 11010
        if not num: return "0"
        
        res = []
        table = "0123456789abcdef"
        
        for i in range(28, -4, -4):
            temp = (num >> i) & 0xf
            res.append(table[temp])
            
        i = 0
        for i in range(8):
            if res[i] != "0": 
                break
        
        return "".join(res[i:])
