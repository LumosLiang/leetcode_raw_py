class Solution:
    def candy(self, ratings: List[int]) -> int:
​
        # O(N), O(N)
        
        res = [1] * len(ratings)
        
        # forward
        
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                res[i + 1] = res[i] + 1
           
        # backward, fix
        
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i] < ratings[i - 1] and res[i] >= res[i - 1]:
                res[i - 1] = res[i] + 1
         
        return sum(res)
    
# class solution:
#     def candy(self, ratings: list[int]) -> int:
​
#         # o(n), o(n)
        
#         res = [0] * len(ratings)
#         res[0] = 1
        
#         # forward
        
#         for i in range(len(ratings) - 1):
#             curr, nxt = ratings[i], ratings[i + 1]
#             if curr < nxt:
#                 res[i + 1] = res[i] + 1
#             elif curr == nxt:
#                 res[i + 1] = 1
#             else:
#                 if curr > 1:
#                     res[i + 1] = res[i] - 1
#                 else:
#                     res[i + 1] = 1
        
#         print(res)
        
#         # backward, fix
        
#         for i in range(len(ratings) - 1, 0, -1):
#             curr, pre = ratings[i], ratings[i - 1]
​
#             if curr < pre:
#                 if res[i] == res[i - 1]:
#                     res[i - 1] = res[i] + 1