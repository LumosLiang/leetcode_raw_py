class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        return self.sol1(strs)
    
    # one by one
    # 先放进去的技巧，merge interval学的
    def sol1(self, strs):
        
        def get_common(s1, s2):
            p1, p2 = 0, 0
​
            while p1 < len(s1) and p2 < len(s2):
                if s1[p1] != s2[p2]:
                    return s1[:p1]
                p1 += 1
                p2 += 1
​
            return s1 if p1 == len(s1) else s2
    
        curr = strs[0]
        for i in range(1, len(strs)):
            nxt = strs[i]
            curr = get_common(curr, nxt)
            
        return curr
        
    
    # O(wordleng * logN)
    # divide and conquer
    def sol2(self, strs):
        
        def helper(strs, left, right):
            
            if left == right: return strs[left]
            
            def get_common(s1, s2):
                
                p1, p2 = 0, 0
                
                while p1 < len(s1) and p2 < len(s2):
                    if s1[p1] != s2[p2]:
                        return s1[:p1]
                    p1 += 1
                    p2 += 1
                
                return s1 if p1 == len(s1) else s2
                
            mid = (left + right) // 2
            
            l_LCP = helper(strs, left, mid)
            r_LCP = helper(strs, mid + 1, right)
            
            return get_common(l_LCP, r_LCP)
        
        return helper(strs, 0, len(strs) - 1)
