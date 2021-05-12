class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        l = len(mat[0])
        w = len(mat)
        
        mat_idx = [[[i,j] for j in range(l)] for i in range(w)]
        diag = mat_idx[0][1:] + [m[0] for m in mat_idx]
        
        for d in diag:
            tcx, tcy, tv = [], [], []
            i, j = d[0], d[1]
            
            while 0 <= i <= w - 1 and 0 <= j <= l - 1:
                tcx.append(i)
                tcy.append(j)
                tv.append(mat[i][j])
                i += 1
                j += 1
​
            tv.sort()
            for t in range(len(tv)):
                mat[tcx[t]][tcy[t]] = tv[t]
                    
        return mat
                
            
