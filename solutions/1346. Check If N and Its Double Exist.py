class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        h = {}
        
        for num in arr:
            if num not in h:
                h[num * 2] = num
                if not num % 2: 
                    h[num // 2] = num
            else:
                return True
            
        return False
