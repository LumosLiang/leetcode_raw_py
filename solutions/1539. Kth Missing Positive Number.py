class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        diff = arr[-1] - len(arr) 
        if diff >= k:
            return sorted(list(set([i for i in range(1, arr[-1] + 1)]) - set(arr)))[k - 1]
        else:
            return arr[-1] + k - diff
            
