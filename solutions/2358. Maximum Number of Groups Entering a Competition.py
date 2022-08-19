class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        l, r = 1, len(grades)
        
        while l < r:
            mid = (l + r) // 2 + 1
            
            least = (1 + mid) * mid // 2
            
            if len(grades) < least:
                r = mid - 1
            else:
                l = mid
                
        return l
​
