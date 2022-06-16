class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # 大数相加的二进制版本。
        
        l1, l2 = len(a), len(b)
        p1, p2, carry = l1 - 1, l2 - 1, 0
        base = ord("0")
        res = []
        
        while p1 >= 0 or p2 >= 0 or carry != 0:
            S = 0
            if p1 >= 0:
                S += ord(a[p1]) - base
                p1 -= 1
            if p2 >= 0:
                S += ord(b[p2]) - base
                p2 -= 1
            if carry > 0:
                S += carry
            
            res.append(str(S % 2))
            carry = S // 2
    
        return "".join(res[::-1])
