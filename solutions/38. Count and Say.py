class Solution:
    def countAndSay(self, n: int) -> str:
        
        res = "1"
        
        for i in range(2, n + 1):
            res = self.say(res)
​
        return res
        
    
    def say(self, s):
        res, count = "", 1
        s += "a"
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                res += str(count) + s[i]
                count = 1
            else:
                count += 1
        
        return res
        
