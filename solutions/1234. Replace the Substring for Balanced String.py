class Solution:
    def balancedString(self, s: str) -> int:
        
        # initial
        # window, need
        # criteria
        # when to update
        
        balanced_val = len(s) // 4
        temp = collections.Counter(s)
        need = {}
        need_counts = 0
        print(temp)
        for key, val in temp.items():
            if val > balanced_val:
                diff = val - balanced_val
                need_counts += diff
                need[key] = diff
        
        if need_counts == 0: return 0
        
        l, min_len, window, match = 0, float('inf'), collections.Counter(), 0
        
        for r, val in enumerate(s):
            if val in need:
                window[val] += 1
                if window[val] == need[val]:
                    match += 1
            
            while match == len(need):
                min_len = min(min_len, r - l + 1)
                if s[l] in need:
                    window[s[l]] -= 1
                    if window[s[l]] < need[s[l]]:
                        match -= 1
                l += 1
                
        return min_len
            
        
        
                
​
        
​
    
        
        
        
        
