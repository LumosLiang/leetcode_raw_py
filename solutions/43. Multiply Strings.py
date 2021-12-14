class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def strToInt(num):
            res, base = 0, 1
            for i in range(len(num) - 1, -1, -1):
                res += base * (ord(num[i]) - ord("0"))
                base *= 10
            return res
            
        n1, n2 = strToInt(num1), strToInt(num2)
​
        def intToStr(num):
            res = ""
            while num:
                temp = num % 10
                res = chr(ord("0") + temp) + res
                num = num // 10
            
            return res if len(res) > 0 else "0"
            
        return intToStr(n1 * n2)
            
            
        
            
            
            
        
