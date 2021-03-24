import collections
​
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if len(s) == 0 or k > len(s):
            return 0
        
        dic = collections.Counter(s)
        
        for i, letter in enumerate(s):
            if dic[letter] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i + 1:], k)
                break
        else:
            return len(s)
        
        return max(left, right)
        
        
