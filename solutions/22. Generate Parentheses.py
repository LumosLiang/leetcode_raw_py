class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(left, right, path):
            if left > right or left < 0 or right < 0:
                return
            if left == right == 0:
                self.res.append(path)
            backtrack(left - 1, right, path + '(')
            backtrack(left, right - 1, path + ')')
        
        self.res = []
        backtrack(n, n, '')
        return self.res
