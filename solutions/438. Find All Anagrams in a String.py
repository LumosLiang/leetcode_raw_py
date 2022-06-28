class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
​
    # anagrams: keys are same, values are same
    
    # 明确这是一个sliding window问题
    # 单调性体现在：一旦这些字母能够被囊括，那么剩下的事情就是我要在这个区间进行搜索。缩小到一个区间，
    # 在这个区间中，字母一样，频率一样。这就是答案，然后left + 1
    # 我们需要什么
        # p的key，和freq。window的key和frequ，进入和跳出区间的条件
    
        window = collections.Counter()
        need = collections.Counter(p)
        l = 0
        res = []
        match_cnt = 0
​
        for r, val in enumerate(s):
            window[val] += 1
​
            if val in need and window[val] == need[val]:
                match_cnt += 1
​
            # 当前的window一定包含所有的key，且每一个key的个数都会至少等于need中对应的个数
            
            while match_cnt == len(need):
                
                # if r - l + 1 == len(p):
                if len(window) == len(need) and all([window[key] == need[key] for key in window]):
                    res.append(l)    
                    
                window[s[l]] -= 1
                
                if s[l] in need and window[s[l]] < need[s[l]]:
                    match_cnt -= 1
​
                if window[s[l]] == 0:
                    del window[s[l]]
​
                l += 1
                
​
        return res
    
    
