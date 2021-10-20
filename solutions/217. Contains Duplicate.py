class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(nums) != len(set(nums))
​
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hash = collections.Counter(nums)
        
        for val in list(hash.values()):
            if val != 1: 
                return True
                break
        
        return False
