class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        
        # [[0,2],[5,10],[13,23],[24,25]]
        # [[1,5],[8,12],[15,24],[25,26]]
        
        # merge interval + merge list
        # 1. every time, I get a interval [max, min]
        # if has interval, append, 
        # if min is A's right, pa ++
        # else: pb ++
​
                
        p1, p2 = 0, 0
        res = []
        
        while p1 < len(firstList) and p2 < len(secondList):
            
            interv1, interv2 = firstList[p1], secondList[p2]
            intersect = [max(interv1[0], interv2[0]), min(interv1[1], interv2[1])]
​
            if intersect[0] <= intersect[1]: res.append(intersect)
            
            if interv1[1] <= interv2[1]:
                p1 += 1
            else:
                p2 += 1
​
        return res
