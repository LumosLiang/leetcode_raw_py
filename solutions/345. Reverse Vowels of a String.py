class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        ls = list(s)
        l, r = 0, len(s) - 1
        while l <= r:
            if ls[l] in v and ls[r] in v:
                ls[l], ls[r] = ls[r], ls[l]
                l += 1
                r -= 1
            elif ls[l] in v: r -= 1
            elif ls[r] in v: l += 1
            else:
                l += 1
                r -= 1
                
        return ''.join(ls)
                
            
                
