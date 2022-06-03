class Solution:
    def isHappy(self, n: int) -> bool:
        return self.sol2(n)
    
    # 
    def sol1(self, n):
        
        def sum_of_square_digit(num):
            
            res = 0
            while num:
                num, digit = num // 10, num % 10
                res += digit ** 2
            
            return res

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
                
    # slow, fast pointer.    
    def sol2(self, n):
        
        def helper(num):
            res = 0
            while num:
                num, digit = num // 10, num % 10
                res += digit ** 2
            
            return res

        slow, fast = n, n
        
        while True:
            
            slow = helper(slow)
            fast = helper(helper(fast))
            
            if fast == 1: return True
            if slow == fast: return False
