class Solution:
    def isHappy(self, n: int) -> bool:
        
        # 2 -> 4 -> 16 -> 36 + 1 -> 9 + 49 58 -> 25 + 64 89-> 64 + 81 145-> 1 + 16 + 25 42 -> 16 + 4 20 -> 4   
        # Non-happy的数字 会在一个循环内
        
        
        def sum_of_square_digit(num):
            
            res = 0
            while num:
                num, digit = num // 10, num % 10
                res += digit ** 2
            
            return res
​
        s = set()
        s.add(n)
        
        while True:
            curr_val = sum_of_square_digit(n)
            if curr_val == 1:
                return True
            elif curr_val in s:
                return False
            else:
                s.add(curr_val)
                n = curr_val
        
                
