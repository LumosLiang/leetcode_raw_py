class Solution:
   
    def wordBreak(self, s: str, wordDict):
        
        l = len(s)
        dp = [[""]]
        
        for i in range(len(s) - 1, -1, -1):
            temp = []
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict and dp[l - j]:
                    for item in dp[l - j]:
                        if item == "":
                            temp.append(s[i:j])
                        else:
                            temp.append(s[i:j] + " " + item)
            dp.append(temp)
        return dp[-1]
