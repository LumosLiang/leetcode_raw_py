class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        left = right = 0
        minlen = float('Inf')
        start = 0
        
        need = collections.Counter(t)
        window = collections.Counter()
        
        match = 0
        while right < len(s):
            temp1 = s[right]
            if need[temp1]:
                window[temp1] += 1
                if window[temp1] == need[temp1]:
                    match += 1
            right += 1
            
            while match == len(need):
                if right - left < minlen:
                    minlen = right - left
                    start = left
                temp2 = s[left]
                if need[temp2]:
                    window[temp2] -= 1
                    if window[temp2] < need[temp2]:
                        match -= 1
                left += 1
        return s[start:start + minlen] if minlen != float('Inf') else ""
​
