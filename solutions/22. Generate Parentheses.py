class Solution:
    def generateParenthesis1(self, n: int) -> List[str]:
        
        res = []
        
        def backtrack(left, right, path):
            if left < 0 or right < 0 or right < left:
                return
            
            if left == right == 0:
                res.append(path)
            
            backtrack(left - 1, right, path + "(")
            backtrack(left, right - 1, path + ")")
        
        backtrack(n, n, "")
        return res
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        dp = [[""]]
        
        for i in range(1, n + 1):
            temp = []
            for j in range(i):
                # (f(i))f(j)  0 <= j <= i - 1
                for x in dp[j]:
                    for y in dp[-j-1]:
                        temp.append(f"({x}){y}")
            
            dp.append(temp)
        return dp[-1]
    
​
