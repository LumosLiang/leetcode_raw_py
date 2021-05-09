class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        
        for i, c in enumerate(costs):
            coins -= c
            if coins < 0: return i
            
        return len(costs)
