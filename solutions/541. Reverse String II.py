class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        return self.sol2(s, k)
        # O(N), O(N)
    def sol1(self, s, k):  
        def reverse(s, left, right):
            
            if left >= right: return
            
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        s = list(s)
        l = len(s)
        cnt = 0
        
        while cnt < l // (2 * k):
            base = cnt * (2 * k)
            reverse(s, base,  base + k - 1)
            cnt += 1
       
        if l - cnt * (2 * k) >= k:
            reverse(s, cnt * (2 * k), cnt * 2 * k + k - 1)
        else:
            reverse(s, cnt * (2 * k),  l - 1)
        
        return "".join(s)
         
    # better one? 
    def sol2(self, s, k):
        
        def reverse(s, left, right):
            
            if left >= right: return
            if right > len(s) - 1: right = len(s) - 1
            
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        s = list(s)
        l = len(s)
        
        for i in range(0, l, 2 * k):
            reverse(s, i, i + k - 1)
        
        return "".join(s)
        
        
        
            
            
