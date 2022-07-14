class UnionFind:
    
    def __init__(self, cnt):
        self.root = [i for i in range(cnt)]
        self.rank = [1 for i in range(cnt)]
        self.size = cnt
        
    def find(self, x):
        if x == self.root[x]: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
            self.size -=1
                
        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
         
        if not pairs: return s
    
        l = len(s)
        uf = UnionFind(l)
        for pair in pairs:
            x, y = pair[0], pair[1]
            uf.union(x, y)
        
        if uf.size == 1: return "".join(sorted(s))
        
        hash_val = collections.defaultdict(list)
        hash_idx = collections.defaultdict(list)
        
# hash {root: heap()}
#         for i in range(len(s)):
#             root = uf.find(i)
#             heapq.heappush(hash_val[root], s[i])
#             heapq.heappush(hash_idx[root], i)
​
#         res = l * [0]
        
#         for k, v in hash_idx.items():
#             while v:
#                 idx = heapq.heappop(v)
#                 val = heapq.heappop(hash_val[k])
#                 res[idx] = val
        
#         return "".join(res)
            
#                 hash_val = collections.defaultdict(list)
#         hash_idx = collections.defaultdict(list)
        
        for i in range(len(s)):
            root = uf.find(i)
            hash_val[root].append(s[i])
            hash_idx[root].append(i)
​
        res = l * [0]
        
        for k, v in hash_val.items():
            v.sort()
            for i in range(len(v)):
                res[hash_idx[k][i]] = v[i]
        
        return "".join(res)
            
        
        
        
        
