class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
          
    
        even, odd = 0, 1
        while even < len(A) and odd < len(A):
            if A[even] % 2 == 0: even += 2
            elif A[odd] % 2 == 1: odd += 2
            else: A[even], A[odd] = A[odd], A[even]
        return A
​
        
