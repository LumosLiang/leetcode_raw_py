class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
#         [[10,16],[2,8],[1,6],[7,12]]
        
#                   10 ----- 16
#               5------12
#           1----6
#                         13------22
#                    11----14
#                  7----- 13
            
#         [1,6][2,8][4,12][10,16]
        
        
        points.sort()
        
#         overlap = [points[0][0], points[0][1]]
 
#         res = 0
#         for i in range(1, len(points)):
#             curr = points[i]
#             if curr[0] <= overlap[1]:
#                 overlap = [curr[0], min(overlap[1], curr[1])]
#             else:
#                 overlap = [curr[0], curr[1]]
#                 res += 1
            
#         return res + 1
    
        right = points[0][1]
 
        res = 0
        for i in range(1, len(points)):
           
            if points[i][0] <= right:
                right = min(right, points[i][1])
            else:
                right = points[i][1]
                res += 1
            
        return res + 1
