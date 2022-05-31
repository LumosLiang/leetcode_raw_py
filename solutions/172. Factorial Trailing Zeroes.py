class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        # 5 * 4 * 3 * 2 * 1
        
        # 25
        # 1,2,5,6,8,10,12,13,14,15,16,17,18.19,20,21,22,23,24,25
        
        return self.sol2(n)
        
    def sol1(self, n):
        cnt = 0
        for i in range(1, n + 1):
            while not i % 5:
                cnt += 1
                i = i // 5
        return cnt
    
    def sol2(self, n):
        
        res = 0
        while n > 0:
            n = n // 5
            res += n
        
        return res
