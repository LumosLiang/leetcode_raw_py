class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 异或运算 1的个数
        
        return list(bin(x ^ y)).count('1')
        
