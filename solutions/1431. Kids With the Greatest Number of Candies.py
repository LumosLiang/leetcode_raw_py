class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        
        m = max(candies) - extraCandies 
        return [c >= m for c in candies]
            
