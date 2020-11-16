class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        odds = sum(v % 2 for v in list(collections.Counter(s).values()))
        return len(s) if odds <= 1 else len(s) - odds + 1
    
        
             
