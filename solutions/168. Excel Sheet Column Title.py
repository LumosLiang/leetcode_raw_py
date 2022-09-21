class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        
        # print(chr(base + 24))
        # 10 digit to 26
        
        base = ord('A')
        res = ""
        
        while columnNumber:
            
            columnNumber -= 1
            
            r, q = columnNumber % 26, columnNumber // 26
            
            res = chr(base + r) + res
            columnNumber = q
            
        return res
        
        
