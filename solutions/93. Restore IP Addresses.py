class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # backtrack
        
#         "101023"
#         /   |   \
#        1   10     101 
#   / | \  / | \    / | \
#  0  X X  1 10 102 0 X  X
​
#  1. 每一步都有选择，最多可以选3个digit，最少选一个
#  2. 如果这一步是0，这一步只能选0，没有其他选择
#  3. 必须要有四块，才能符合要求
​
        res = []
        
        # backtrack 是当前 在idx处，你可以给我多少个答案
        def backtrack(idx, path, cnt):
            nonlocal s
            
            if idx == len(s):
                if cnt == 4: 
                    res.append(path.rstrip('.'))
                return
            
            if s[idx] == "0":
                backtrack(idx + 1, path + s[idx] + ".", cnt + 1)
                return
            
            for i in range(1, 4):
                if idx + i < len(s) + 1:
                    temp = s[idx: idx + i]
                    if int(temp) < 256:
                        backtrack(idx + i, path + temp + ".", cnt + 1)
                
               
        backtrack(0, "", 0)
        return res
