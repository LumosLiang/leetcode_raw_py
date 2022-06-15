class Solution:
    def reverseWords(self, s: str) -> str:
        
        # 1. 前后remove 0， 重新定义start, end
        
        # 2， 反转
        
        # 3. 从新的start开始扫 到end结束，in-place的trim中间的0。最终可以得到一个 start, p2
        
        # 4, 然后依次reverse
        
        # return s[start, p2] 就好了
        
        def reverse(l, r):
            while l <= r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        
        s = list(s)
          
        # two pointers to trim left
        start, end = 0, len(s) - 1
        while s[start] == " ":start += 1
        while s[end] == " ": end -= 1
            
        # then get start, end, which is the real start and end of the string
        reverse(start, end)
        
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
        end = p1
        
        p1, p2 = start, start
        while p2 < end:
            if s[p2] == " ":
                reverse(p1, p2 - 1)
                p1 = p2 + 1
            elif p2 == end - 1:
                reverse(p1, p2)
            p2 += 1
        
        return "".join(s[start:p2])
