class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # donot create more space in memory?
        
        for i in range(len(A)):
            # do horizontal job
            A[i] = list(reversed(A[i]))
            # do invert job, abs
            
            A[i] = [abs(j-1) for j in A[i]]
            
        return A
    
