class Solution:
​
            
    def subStrHash(self, s, p, m, k, hashValue):
        def val(c):
            return ord(c) - ord('a') + 1
            
        n = len(s)
        b = 1
        cur = 0
        res = n - k
​
        for i in range(n - k, n):
            cur = (cur + val(s[i]) * b) % m
            b = b * p % m
​
        for i in range(n - k - 1, -1, -1):
            cur = (cur * p + val(s[i]) - val(s[i + k]) * b) % m
            if cur == hashValue:
                res = i
        return s[res: res + k]
        
