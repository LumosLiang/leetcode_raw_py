class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        count = [0] * (n + 1)
        for t in trust:
            count[t[0]] -= 1
            count[t[1]] += 1
        
        for i in range(1, len(count)):
            if count[i] == n -1:
                return i
        return -1
        
                
