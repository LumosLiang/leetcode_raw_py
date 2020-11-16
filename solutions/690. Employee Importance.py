"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
​
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        hash = {employee.id: [employee.importance, employee.subordinates] for employee in employees}
    
        res, q = [],[id]
        
        while q:
            temp_e = q.pop()
            res.append(hash[temp_e][0])
            for sub in hash[temp_e][1]:
                q.append(sub)
                
        return sum(res)
            
        
        
            
                
        
        
        
        
