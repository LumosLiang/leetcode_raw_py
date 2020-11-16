class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        if len(numbers) <= 1: return []
        
        hash = {}
        
        for i in range(len(numbers)):
            if numbers[i] in hash:
                return [hash[numbers[i]] + 1, i + 1]
            else:
                hash[target - numbers[i]] = i
                
