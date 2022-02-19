class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        even, res = [], []
        
        if not l % 2:
            even = [nums[2 * i] for i in range(l // 2)]    
        else:
            even = [nums[2 * i] for i in range(l // 2 + 1)]
            
        odd = [nums[2 * i + 1] for i in range(l // 2)]
        
        even.sort()
        odd.sort(reverse = True)
            
        for i in range(l // 2):
            res.append(even[i])
            res.append(odd[i])
​
        return res if not l % 2 else res + [even[-1]]
            
