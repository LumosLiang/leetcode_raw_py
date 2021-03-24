class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        b_s = bin(n)[3:]
        return n !=0 and '1' not in b_s and len(b_s)%2 == 0
