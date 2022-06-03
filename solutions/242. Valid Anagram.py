class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort
        # hash
        # follow up -> hash + default list
    
        return self.sol2(s, t)    
        
    def sol1(self, s, t):
        # O(NlogN + MlogM)
        return sorted(s) == sorted(t)
    
    
    def sol2(self, s, t):
        # O(N + M)
        
        hash_s = collections.Counter(s)
        hash_t = collections.Counter(t)

        for ks, vs in hash_s.items():
            if ks not in hash_t or hash_t[ks] != vs:
                return False
            del hash_t[ks]
        return not hash_t
        
    def sol3(self, s, t):
        
        dit = {}
        
        # set
        for i in s:
            if i in dit:
                dit[i] += 1
            else:
                dit[i] = 1
        
        # cancel
        for j in t:
            if j not in dit:
                return False
            else:
                dit[j] -= 1
        
        # compare
        for k, v in dit.items():
            if v != 0:
                return False
        
        return True
