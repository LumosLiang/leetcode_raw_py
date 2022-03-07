class Solution:
    # O(logN^2) why?, O(1)
    # inner loop: logN, outter loop, logN
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2 ** 31 and divisor == -1: return 2** 31 - 1
        
        sign = (dividend > 0) == (divisor > 0)
        
        divd, divs = abs(dividend), abs(divisor)
        
        res = 0
        
        while divd >= divs:
            temp, cnt  = divs, 1
            
            while divd >= temp:
                divd -= temp
                res += cnt
                cnt <<= 1
                temp <<= 1
​
        if sign: return res
        else: return -res
