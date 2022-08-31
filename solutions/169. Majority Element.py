class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.sol4(nums)
    # hash, brute force, divde and conquer
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
    def sol3(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
    # bit
    # O(32 * N), O(1)
    def sol4(self, nums):
        bit = 32 * [0]
        for num in nums:
            for i in range(32):
                if num >> (31 - i) & 1:
                    bit[i] += 1
        
        ans, l = 0, len(nums)
        
        for i in range(32):
            if bit[i] > l // 2:
                ans +=  1 << (31 - i)
                # ans += 1 * 2 ** (31 - i)
        return ans
       
    def sol5(self, nums):
        res = 0
        for i in range(32):
            temp = 0
            for num in nums:
                if num >> (31 - i) & 1:
                    temp += 1
                    
            if temp > (len(nums) // 2):
                res += 1 << (31 - i) 
        
        return res
        
