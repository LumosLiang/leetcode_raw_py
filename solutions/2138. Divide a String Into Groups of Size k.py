class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        res = []
        temps = ''
        
        for i in range(len(s)):
            
            if i % k == 0:
                temps = s[i]
            else:
                temps += s[i]
                
            if i == len(s) - 1 and len(temps) < k:
                temps += (k - len(temps)) * fill
            if len(temps) == k:
                res.append(temps)
            
        return res
