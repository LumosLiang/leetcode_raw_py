class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        # find all key
        all_key = []
        for i in range(len(nums)):
            if nums[i] == key:
                all_key.append(i)
                
        # output res
        res = []
        for i in all_key:
            res += [j for j in range(i - k, i + k + 1) if j >= 0 and j < len(nums)]
            
        return set(res)
                
        
