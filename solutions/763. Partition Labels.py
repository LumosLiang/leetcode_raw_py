class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        "ababcbaacdefegdehijhklij"
        # Greedy: at most 1 part, as mamy parts as possible\
        
        # 1. O(N) -> hash{letter:last_appear_pos}
        # 2. loop, two-pointers
        # O(N), O(N)
        
        latest_seen = {}
        for idx, val in enumerate(s):
            latest_seen[val] = idx
        
        l = 0
        res = []
        right_bound = latest_seen[s[l]]
        
        for r, val in enumerate(s):
            if r < right_bound:
                right_bound = max(right_bound, latest_seen[val])
            elif r == right_bound:
                res.append(r - l + 1)
                l = r + 1
                if l < len(s):
                    right_bound = latest_seen[s[l]]
                
        return res                                                  
        
