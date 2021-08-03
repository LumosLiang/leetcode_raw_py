class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        def biseleft(nums, x):
            lo, hi = 0, len(nums) - 1
    
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] >= x: hi = mid
                else: lo = mid + 1
            
            return lo
        
        idx = biseleft(arr, x)
        if idx > 0 and arr[idx] + arr[idx-1] >= 2*x:
            idx -=1
        
        l, r = idx, idx
​
        
        while k - 1:
            if l == 0: r += 1
            elif r == len(arr) - 1: l -= 1
            else:
                if abs(arr[l - 1] - x) <= abs(arr[r + 1] - x):  l -= 1
                else: r += 1
                
            k -= 1
           
        return arr[l: r + 1]
​
