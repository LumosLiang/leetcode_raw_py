class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        return self.solution2(numbers, target)
    
    # T O(N), S: O(1)
    def solution1(self, numbers: List[int], target: int):
        
        l, r = 0, len(numbers) - 1
        
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target: return [l + 1, r + 1]
            elif s > target: r -= 1
            else: l += 1
    
    # T: O(N), S: O(N)
    def solution2(self, numbers: List[int], target: int):
        
        H = {}
        
        for i in range(len(numbers)):
            if numbers[i] in H:
                return [H[numbers[i]] + 1, i + 1]
            else:
                H[target - numbers[i]] = i
                
        
