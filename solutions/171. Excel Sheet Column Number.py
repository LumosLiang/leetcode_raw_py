class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
#         R S T U V W X Y Z
#         18  19  20  21  22  23  24 25 26
        
#         "RXW"
        
#         W + X * 26 + R * 26 ^2
​
​
        res, base = 0, 26
    
        for c in columnTitle:
            
            res = res * base + (ord(c) - ord('A') + 1)
        
        return res
    # 23 + 24 * 26 + 18 * (26 ** 2)
        
        
