class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return self.sol2(num1, num2)
    
    def sol1(self, num1: str, num2: str):
        l1, l2 = len(num1), len(num2)
        p1, p2, carry = l1 - 1, l2 - 1, 0
        base = ord("0")
        res = [""] * (max(l1, l2) + 1)
        p = len(res) - 1
        
        while p1 >= 0 or p2 >= 0 or carry != 0:
            
            # p1 p2 在范围内
            # p1 或 p2 在范围内
            # p1 p2都不在，但是carry依然有值没解决
            
            if p1 >= 0 and p2 >= 0:
                S = ord(num1[p1]) - base + ord(num2[p2]) - base + carry
                res[p] = S % 10
                carry = S // 10
                p -= 1
                p1 -= 1
                p2 -= 1
            elif p1 >= 0:
                S = ord(num1[p1]) - base + carry
                res[p] = S % 10
                carry = S // 10
                p -= 1
                p1 -= 1
            elif p2 >= 0:
                S = ord(num2[p2]) - base + carry
                res[p] = S % 10
                carry = S // 10
                p -= 1
                p2 -= 1
            else:
                res[p] = str(carry)
                carry = 0
        ans = ""
        for r in res:
            if r != "": ans += str(r)
        return ans
    
    # 简洁写法
    def sol2(self, num1: str, num2: str):
        l1, l2 = len(num1), len(num2)
        p1, p2, carry = l1 - 1, l2 - 1, 0
        base = ord("0")
        res = [""] * (max(l1, l2) + 1)
        p = len(res) - 1
        
        while p1 >= 0 or p2 >= 0 or carry != 0:
            S = 0
            if p1 >= 0:
                S += ord(num1[p1]) - base
                p1 -= 1
            if p2 >= 0:
                S += ord(num2[p2]) - base
                p2 -= 1
