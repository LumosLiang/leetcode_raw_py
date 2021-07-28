class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def backtrack(choices, path, s, p):
            if p == len(s):
                temp =True
                for p in path:
                    temp *= p[::] == p[::-1]
                if temp: res.append(path)
                return
            
            for c in choices:
                temp = path[::]
                if not c:temp.append(s[p])
                else: temp[-1] += s[p]
                backtrack(choices, temp, s, p + 1)
                    
        backtrack([0,1], [s[0]], s, 1)
                
        return res                                                                                                                              
