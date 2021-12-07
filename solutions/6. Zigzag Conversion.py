 # the unit length of a zigzag is (numRows - 1) * 2 whne numRows != 1
        
        # partition the string in unit length, complete the string length with empty string "" until the last unit satisfy the unit length
        # in each partition:    
            # exclude the first
            # find the mid, and then do two pointer for each row.
​
class Solution:
    def convert(self, s: str, numRows: int) -> str:
            
        if numRows == 1 or numRows >= len(s): return s
        
        unitL = 2 * (numRows - 1)
        
        s += " " * (unitL - (len(s) % unitL))
        
        res = [""] * numRows
        
        for i in range(len(s) // unitL):
            temp = self.processUnit(s, unitL * i, unitL* (i + 1) - 1)
            for j in range(numRows):
                if temp[j] != " ":
                    res[j] += temp[j]
            
        return "".join(res)
    
    def processUnit(self, s, start, end):
        
        res = [s[start]]
        mid = (start + end)// 2 + 1
        l, r = start + 1, end
        
        while l < r:
            ls, rs = s[l], s[r]
            if ls != " " and rs != " ": res.append(ls + rs)
            elif ls != " ": res.append(ls)
            elif rs != " ": res.append(rs)
            else: res.append(" ")
            l += 1
            r -= 1
        
        res.append(s[mid])    
        return res
​
