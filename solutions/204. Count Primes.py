class Solution:
    def countPrimes(self, n: int) -> int:
​
        if n <= 2:
            return 0
        dp = [1] * n
        dp[0] = dp[1] = 0
        for i in range(2, n):
            if dp[i]:
                for j in range(2 * i, n, i):
                    dp[j] = 0
        return sum(dp)
​
