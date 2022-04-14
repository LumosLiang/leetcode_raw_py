class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        # the recognization on the legal pair
        # dp:
            # dp[i]: at point i, the longest Valid Parentheses I can acheive.
            # base: dp[0] = 0
            # fuction: 
                # dp[i] = dp[j] + i - j + 1
                # where between i and j, they are all legal pair. 
                # So that is why we shoud put idx into stack and, compute the difference.
        
        # O(N), O(N)
        stack = []
        dp = [0] * (len(s) + 1)
        
        for i, c in enumerate(s):
            # I only focus on the first c,
            if c == "(":
                stack.append(i)
            else:
                if stack:
                    j = stack.pop()
                    dp[i + 1] = i - j + 1 + dp[j]
        
        return max(dp)
                
