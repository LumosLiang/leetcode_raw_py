class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        cnt = 0
    
        for n in nums:
            temp = 0
            
            while n:
                n = n // 10
                temp += 1
            
            if not temp % 2:
                cnt += 1
            
        return cnt
