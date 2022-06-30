class Solution:
    def countSubstrings(self, s: str) -> int:
        # permutation + isPalindromic?
        
        return self.sol2(s)
    
    # brute force
    # O(N^2)
    def sol1(self, s):
        
        def helper(l, r):
            nonlocal s
            
            ans = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            return ans
        
        res = 0
        for i in range(len(s)):
            res += (helper(i, i) + helper(i, i + 1))
        
        return res
​
    # brute force
    # O(N^3)
    def sol2(self, s):
        
        res = 0
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    res += 1
        return res
