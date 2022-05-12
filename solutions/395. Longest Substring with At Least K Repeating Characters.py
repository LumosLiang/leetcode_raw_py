        l = 0 
        for r, val in enumerate(s):
            
            if freq_cnt[val] < k:
                res = max(res, self.sol2(s[l:r], k))
                l = r + 1
                
        res = max(res, self.sol2(s[l:r + 1], k))
        return res      
        
    # sliding window
    # window -> hash
    # shrink 这里没有办法shrink，因为我们无法舍弃左区间，也还要继续像右边的区间走。
    # 所以我们需要加条件来限制：限制出现的元素数
    # 比如，"aaabccccbaaaaaa"，只能出现1个~26个distinct元素的情况下，找到"最长的至少包含k个重复的子串"
    # 为什么这样可以？
    # 怪不得是 340
    
    def sol3(self, s, k):
        
        # Longest Substring (with At Least K Repeating Characters) with exactly K distinct char
        
        def helper(s, k, cnt):
            res = 0
            window = collections.defaultdict(int)
            l = 0
            match_cnt = 0
            
            for r, val in enumerate(s):
                window[val] += 1
                
                if window[val] == k:
                    match_cnt += 1
                    
                if len(window) == cnt and match_cnt == cnt:
                    res = max(res, r - l + 1)
                    
                while len(window) > cnt:
                    window[s[l]] -=1
                    
                    if window[s[l]] == k - 1:
                        match_cnt -= 1
                        
                    if window[s[l]] == 0:
                        del window[s[l]]
                        
                    l += 1
                    
            return res
        
        res = 0
        for i in range(1, 27):
            temp = helper(s, k, i)
            res = max(res, temp)
        
        return res
        
        
        
        
​
