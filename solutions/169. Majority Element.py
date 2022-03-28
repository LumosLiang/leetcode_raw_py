class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
    
    
    
    # O(N), O(1)
    # moore voting
    def majorityElement(self, nums: List[int]) -> int:
        winner = None
        winner_cnt = 0
        
        for num in nums:
            if winner is not None:
                if num == winner:
                    winner_cnt += 1
                else:
                    winner_cnt -= 1
                    if winner_cnt == 0:
                        winner = None
            else:
                winner = num
                winner_cnt += 1
        
        return winner
    
    # Sorting O(NlogN)
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
                
                
