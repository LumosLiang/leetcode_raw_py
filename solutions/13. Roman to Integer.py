class Solution:
    def romanToInt(self, s: str) -> int:
        
        t = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
​
        S, over = 0, 0
        
        for i in range(len(s) - 1):
            pre = t[s[i]]
            lat = t[s[i + 1]]
            if pre < lat:
                over += 2 * pre
            S += pre
        
        return S + t[s[-1]] - over
            
            
        
            
