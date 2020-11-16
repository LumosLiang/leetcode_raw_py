class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # hash table
        # in python, dic is a typical hash table
        
        return sum(k * (k - 1) // 2 for k in collections.Counter(nums).values())
        
        
        
        
