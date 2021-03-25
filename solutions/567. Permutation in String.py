class Solution:
    def checkInclusion(self, s1, s2):
        left, right = 0, 0
        minlen = float('Inf')
        match = 0
​
        needs = collections.Counter(s1)
        window = collections.Counter()
​
        while right < len(s2):
            temp1 = s2[right]
            if needs[temp1]:
                window[temp1] += 1
                if needs[temp1] == window[temp1]:
                    match += 1
            right += 1
            while match == len(needs):
                if right - left < minlen:
                    minlen =  right - left
                temp2 = s2[left]
                if needs[temp2]:
                    window[temp2] -= 1
                    if window[temp2] < needs[temp2]:
                        match -= 1
                left += 1
​
        return True if minlen == len(s1) else False
