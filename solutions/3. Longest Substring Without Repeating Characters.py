import collections
class Solution:
    def lengthOfLongestSubstring(self, s):
        
        left, right = 0, 0
        maxlen = 0
        window = collections.Counter()
        
        while right < len(s):
            temp1 = s[right]
            window[temp1] += 1
            lenw = len(window)
            if lenw > maxlen:
                maxlen = len(window)
                
            right += 1
            while list(window.values()) != [1] * len(window):
                temp2 = s[left]
                
                window[temp2] -= 1
                if window[temp2] == 0:
                    del window[temp2]
                left += 1
            
        return maxlen
​
​
