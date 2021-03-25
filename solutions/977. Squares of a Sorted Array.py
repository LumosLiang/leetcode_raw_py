import math
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lst = []
        for a in A:
            lst.append(int(math.pow(a,2)))
        lst.sort()
        return lst    
