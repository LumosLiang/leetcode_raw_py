class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        arrl = len(arr) 
        
        if arrl < 3: return False
        
        l, r = 0, arrl - 1
        
        while l < arrl - 1 and l <= r and arr[l + 1] > arr[l]:
            l += 1
​
        while r >= 1 and l <= r and arr[r - 1] > arr[r]:
            r -= 1
        
        if l == r and l != 0 and r != arrl - 1: return True
        else: return False
