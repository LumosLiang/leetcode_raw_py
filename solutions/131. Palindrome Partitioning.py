class Solution:
    def partition(self, s: str) -> List[List[str]]:
       
        return self.sol2(s)
         
    def sol1(self, s):
        def isPalindrome(s):
            if not s: return False
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
                
            return True
        
        self.res = []
        # no return
        def backtrack(idx, path):
            nonlocal s
            
            if idx == len(s):
                self.res.append(path)
                return

            for i in range(idx + 1, len(s) + 1):
                if isPalindrome(s[idx:i]):
                    backtrack(i, path + [s[idx:i]])
        
        backtrack(0, [])
        
        return self.res
    
    # dp
    def sol2(self, s):
        
        # dp[i] -> s[i:] 可以得到的所有palindrome
        # dp[i - 1] -> [[s[i - 1:i]] + item for item in dp[i]] if s[i - 1:i] is a palindrome 
        
        def isPalindrome(s):
            if not s: return False
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        dp = [[]] * (len(s) + 1)
        dp[-1] = [[]]

        for i in range(len(s) - 1, -1, -1):
            temp = []
            for j in range(i + 1, len(s) + 1):
                if isPalindrome(s[i:j]):
                    for item in dp[j]:
                        temp.append([s[i:j]] + item)        
            dp[i] = temp
        
        return dp[0]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, l = [], len(s)
        
        def backtrack(i, path):
            nonlocal s
            
            if i == len(s):
                res.append(path)
                return

            for j in range(i + 1, l + 1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    backtrack(j, path + [temp])
        
        backtrack(0, [])
        
        return res
    
