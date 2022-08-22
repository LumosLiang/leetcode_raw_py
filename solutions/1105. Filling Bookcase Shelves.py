class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
    
        return self.sol2(books, shelfWidth)
        # books[:i + 1]的高度
    def sol1(self, books, shelfWidth):
        @lru_cache(None)
        def dfs(i):
            if i == -1: return 0
            if i == 0: return books[i][1]
            
            curr_w, curr_h = books[i][0], books[i][1]
            
            temp = curr_h + dfs(i - 1)
            
            for j in range(i - 1, -1, -1):
                if books[j][0] + curr_w <= shelfWidth:
                    curr_w += books[j][0]
                    curr_h = max(curr_h, books[j][1])
                    
                    temp = min(temp, dfs(j - 1) + curr_h)
                else:
                    break
                    
            return temp
                
                
        return dfs(len(books) - 1)
            
​
        
    def sol2(self, books, shelfWidth):
        
        l = len(books)
        dp = [10 ** 6] * (l + 1)
        
        dp[0] = 0
        dp[1] = books[0][1]
        
        for i in range(2, l + 1):
            
            curr_w, curr_h = books[i - 1][0], books[i - 1][1]
            dp[i] = curr_h + dp[i - 1]
            for j in range(i - 1, -1, -1):
                if books[j - 1][0] + curr_w <= shelfWidth:
                    curr_w += books[j - 1][0]
                    curr_h = max(curr_h, books[j - 1][1])
                    
                    dp[i] = min(dp[i], dp[j - 1] + curr_h)
                else:
                    break
      
        return dp[-1]
        
        
        
​
        
        
        
            
​
