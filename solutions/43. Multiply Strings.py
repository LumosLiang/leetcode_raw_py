class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        return self.sol2(num1, num2)
    
    # 你要明白，之所以可以这样做，是因为Python没有溢出，换了其他的语言，就不可以这样
    def sol1(self, num1: str, num2: str):
        
        def strToInt(num):
            res, base = 0, 1
            for i in range(len(num) - 1, -1, -1):
                res += base * (ord(num[i]) - ord("0"))
                base *= 10
            return res
            
        n1, n2 = strToInt(num1), strToInt(num2)
        
        def intToStr(num):
            res = ""
            while num:
                temp = num % 10
                res += chr(ord("0") + temp)
                num = num // 10
            
            return res if len(res) > 0 else "0"
            
        return intToStr(n1 * n2)
    
    # 每一个digit分别处理的思想，前提就是大数相乘的时候遇到的溢出问题，所以python真的很不好。
    # 当系统中遇到的非常大的数相乘的时候的情况。
    def sol2(self, num1: str, num2: str):
        
        
        # num1 = "123", num2 = "456"
        
        l1, l2 = len(num1), len(num2)
        res = [0] * (l1 + l2)
        base = ord('0')
        
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                
                mul = (ord(num1[i]) - base) * (ord(num2[j]) - base)
                sum = res[i + j + 1] + mul
                res[i + j + 1] = sum % 10
                res[i + j] += sum // 10
            
        ans = ""
        for r in res: ans += str(r)
        
        ans = ans.lstrip('0')
        return "0" if ans == "" else ans
