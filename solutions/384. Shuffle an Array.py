class Solution:
​
    def __init__(self, nums: List[int]):
        self.original = copy.deepcopy(nums)
        self.curr = nums
        self.length = len(nums)
​
    def reset(self) -> List[int]:
        return self.original    
    
    def shuffle(self) -> List[int]:
        for i in range(self.length - 1, -1, -1):
            idx = random.randint(0, i)
            
            self.curr[i], self.curr[idx] = self.curr[idx], self.curr[i]
        
        # random.shuffle(self.curr)
        return self.curr
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
