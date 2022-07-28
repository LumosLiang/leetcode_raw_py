class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # 用移位的方法算
        
        ans = 0
        
        while n:
            ans += n & 1
            n = n >> 1
        
        return ans
