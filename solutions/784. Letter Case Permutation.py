class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        
        res, ans = [], []
        S = list(S)
        letter_idx = [k for k, v in enumerate(S) if (ord(v) >= 65 and ord(v) <= 90) or (ord(v) >= 97 and ord(v) <= 122)]
        
        # a simple subsets
        # this is O(2 ^ N + 1 -  1), O(2^N)
        
        def backtrack(choices, path):
            res.append(path)
            
            for i in range(len(choices)):
                backtrack(choices[i + 1:], path + [choices[i]])
        
        backtrack(letter_idx, [])
        
        # This is O(N) * O(nums(letter) ^ 2)
        for r in res:
            temp = S[:]
            for j in r:
                if  97 <= ord(temp[j]) <= 122:
                    temp[j] = chr(ord(temp[j]) - 32)
                elif  65 <= ord(temp[j]) <= 90:
                    temp[j] = chr(ord(temp[j]) + 32)
            ans.append(''.join(temp))
        return ans
