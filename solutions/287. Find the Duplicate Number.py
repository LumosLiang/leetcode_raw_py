class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        # n + 1
        # [1, n] inclusive
        # There is only one repeated number in nums, return this repeated number.
        # All the integers in nums appear only once except for precisely one integer which appears two or more times

        # sol0: brute force O(N^N), O(1)
        # sol1: sort O(NlogN), O(1)
        # sol2: hash: O(N), O(N)
        # sol3: swap sort, O(N), O(1), exactly same as first missing postive
            # sol4: binary search
            # sol5: bit
            # sol6, fast, slow pointer? 
            
    # [1, 6]
    # [4,5,6,5,5,3,2]
    
        return self.sol6(nums)
    
    def sol3(self, nums):
        
        for i in range(len(nums)):
            while nums[i] != i + 1:
                temp = nums[i] - 1
                if nums[temp] != nums[i]:
                    nums[i], nums[temp] = nums[temp], nums[i]
                else:
                    break
        
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return nums[i]
    
    # [3,1,3,4,2]
    # binary search
    # answer must be in [1, n]
    # 太优美了
    # 在搜索空间内搜索，找到比当前小于等于的数的数目，来判断是不是在这里面。
    def sol4(self, nums):
        
        low, high = 1, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid
                
        return low
    
    # 更优美的快慢指针
    # floyd circle detection
    # [2,5,9,6,9,3,8,9,7,1]
    # 因为存在重复，交点必然是快慢指针的交点
    # 
    def sol6(self, nums):
        
        slow, fast = 0, 0
        
        while True:
            
            slow = nums[slow]
            fast = nums[nums[fast]]
            if nums[slow] == nums[fast]:
                break
        
        slow = 0
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
                
        return slow
        
        
#         while nums[slow] != nums[fast]:
#             slow = nums[slow]
#             fast = nums[fast]
                
#         return nums[slow]
        
