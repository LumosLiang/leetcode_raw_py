class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.sol1(nums)
        
    # O(N), O(1)
    # moore voting
    def sol1(self, nums: List[int]):
        winner = none
        winner_cnt = 0
        
        for num in nums:
            if winner is not none:
                if num == winner:
                    winner_cnt += 1
                else:
                    winner_cnt -= 1
                    if winner_cnt == 0:
                        winner = none
            else:
                winner = num
                winner_cnt += 1
        
        return winner
    
    def sol2(self, nums):
        major = nums[0]
        major_cnt = 1
​
        for i in range(1, len(nums)):
​
            if nums[i] == major:
                major_cnt += 1        
            else:
                major_cnt -= 1
                if major_cnt == -1:
                    major = nums[i]
                    major_cnt = 1
​
        return major
    
    # sorting o(nlogn)
    def majorityelement2(self, nums):
        nums.sort()
        return nums[len(nums)//2]
                
    
​
        
