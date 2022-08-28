class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        res = [-1] * len(arr)
        
        m = res[-1]
        
        for i in range(len(arr) - 1, -1, -1):
            res[i] = m
            m = max(m, arr[i])
            
        return res
        
        
