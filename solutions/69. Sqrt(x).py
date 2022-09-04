class Solution:
    def mySqrt(self, x: int) -> int:
        
        return self.sol1(x)
        
    def sol1(self, x):
        l, r = 0, x
        
        
        while l < r:
            mid = (l + r + 1) // 2
            val = mid ** 2
            
            if val <= x:
                l = mid 
            else:
                r = mid - 1
        
        return l
    
    def sol3(self, x):
        l, r = 0, x
        
        while l < r:
            mid = (l + r) // 2
            val = mid ** 2
            
            if val < x:
                l = mid + 1 
            else:
                r = mid
        
        return l if l ** 2 == x else l - 1
​
    # follow-up: if require the accuracy to decimal or more
    def sol2(self, x, k):
    
        def find_interger(x):
            l, r = 0, x
​
            while l < r:
