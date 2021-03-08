class Solution:
    def intervalIntersection(self, A, B):
        
        res = []
        i, j = 0, 0
        
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            
            if b1 <= a2 and b2 >= a1:
                res.append([max(a1, b1), min(a2, b2)])
            if b2 > a2: i += 1 
            else: j += 1
            
        return res
