# dp or DFS + memo or BFS
​
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
#         self.res = -1
#         self.memo = [-1] * len(questions)
        
#         def backtrack(choices, start, path):
            
#             if start >= len(choices):
#                 return max(self.res, path)
            
#             if start 
            
#             for i in range(start, len(questions)):
#                 p = questions[i][0]
#                 exc = questions[i][1]
​
#                 backtrack(questions, exc + i + 1, path + p)
            
        
#         backtrack(questions, 0, 0)
            # [[21,2],[1,2],[12,5],[7,2],[35,3],[32,2],[80,2],[91,5],[92,3],[27,3],[19,1],[37,3],[85,2],[33,4],[25,1],[91,4],[44,3],[93,3],[65,4],[82,3],[85,5],[81,3],[29,2],[25,1],[74,2],[58,1],[85,1],[84,2],[27,2],[47,5],[48,4],[3,2],[44,3],[60,5],[19,2],[9,4],[29,5],[15,3],[1,3],[60,2],[63,3],[79,3],[19,1],[7,1],[35,1],[55,4],[1,4],[41,1],[58,5]]
#         return self.res
            
            
        l = len(questions)
        dp = [-1] * l
        dp[-1] = questions[-1][0]
        
        for i in range(l - 2, -1, -1):
            temp = 0
            start = questions[i][1] + i + 1
            
            if start < l:
                dp[i] = max(questions[i][0] + dp[start], dp[i+1])
            else:  
                dp[i] = max(questions[i][0], dp[i + 1])
            
        return dp[0]
            
            
