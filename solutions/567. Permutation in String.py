class Solution:
    def checkInclusion(self, s1, s2):
        
        # O(len(s1) + len(s2)), O(len(s1) + len(s2))
        
        l, match, min_len = 0, 0, float('inf')
        
        needs = collections.Counter(s1)
        window = collections.Counter()
        
        for r, val in enumerate(s2):
            window[val] += 1
            if val in needs and needs[val] == window[val]:
                match += 1
            
            while match == len(needs):
                min_len = min(min_len, r - l + 1)
                if s2[l] in needs:
                    window[s2[l]] -= 1
                
                if window[s2[l]] < needs[s2[l]]:
                    match -= 1 
                
                l += 1
        
        return True if min_len == len(s1) else False
        
