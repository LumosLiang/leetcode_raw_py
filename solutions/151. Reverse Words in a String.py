class Solution:
    def reverseWords(self, s: str) -> str:
        
        # O(N), O(N)
        # Python cannot do reassign in string
        
        # reverse
        s = list(s)
        
        def reverse(l, r):
            while l <= r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
                
        reverse(0, len(s) - 1)
        
        # two pointers to trim left, seems no need to trim right
        start, end = 0, len(s) - 1
        while s[start] == " ":
            start += 1
        
        while s[end] == " ":
            end -= 1
            
        # then get start, end, which is the real start and end of the string
        # then use two pointer to trim middle
        
        p1, p2 = start, start
        while p2 <= end:
            if s[p2] == " ":
                s[p1] = s[p2]
                p1 += 1
                while p2 <= end and s[p2] == " ":
                    p2 += 1
            else:
                s[p1] = s[p2]
                p1 += 1
                p2 += 1
        
        # then use two pointer to reverse
        p3, p4 = start, start
        
        while p4 < p1:
            if s[p4] == " ":
                reverse(p3, p4 - 1)
                p3 = p4 + 1
            elif p4 == p1 - 1:
                reverse(p3, p4)
            p4 += 1
        
        return "".join(s[start:p1])
            
        
        
