class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        return self.sol1(arr)
        
    def sol1(self, arr: List[int]):
        arrl = len(arr) 
        
        if arrl < 3: return False
        
        l, r = 0, arrl - 1
        
        while l <= r - 1 and arr[l + 1] > arr[l]:
            l += 1
​
        while r >= 1 and arr[r - 1] > arr[r]:
            r -= 1
        
        if l == r and l != 0 and r != arrl - 1: return True
        else: return False
        
        
#     def sol2(self, arr: List[int]):
        
#         arrl = len(arr) 
        
#         if arrl < 3: return False
        
#         l, r = 0, arrl - 1
        
#         while l < r:
            
#             if l < r and arr[l] < arr[l + 1]:
#                 l += 1
#             else:
#                 return False
            
#             if l < r and arr[r] < arr[r - 1]:
#                 r -= 1
#             else:
#                 return False
            
        
#         return True
