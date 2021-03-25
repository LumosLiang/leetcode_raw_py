class Solution:
    def kWeakestRows(self, mat, k):
        #  mat: List[List[int]], 
        #  k: int
        dic, res = {}, []
        
        for row_idx in range(len(mat)):
            zero_idx = self.binsearch(mat[row_idx])
​
            # this problem is actually sort a dic by key then value.
            if zero_idx not in dic.keys():
                dic[zero_idx] = [row_idx]
            else:
                dic[zero_idx].append(row_idx)
​
        for key in sorted(dic):
            res += dic[key]
        
        return res[:k]
​
    def binsearch(self, row):
        # search the index of the first 0.
        low = 0
        high = len(row) - 1
        while low < high:
            mid = low + (high - low) // 2
            if row[mid] == 1: low = mid + 1
            elif row[mid] == 0: high = mid
        if row[low] == 1: return low + 1
        else: return low
​
