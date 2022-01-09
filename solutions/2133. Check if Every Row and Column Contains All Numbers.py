class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        temp = True
        l = len(matrix)
        
        for i in range(l):
            temp = temp * self.check(matrix[i], l)
            if not temp:
                return False
            
        for j in range(l):
            col = []
            for k in range(l):
                col.append(matrix[k][j])
            temp = temp * self.check(col, l)
            if not temp:
                return False
                      
        return True
        
    def check(self, lst, l):
        if len(set(lst)) == l and min(lst) == 1 and max(lst) == l:
            return True
        return False
    
    
