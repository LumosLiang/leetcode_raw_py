class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         [1,2,3,4]
#         1, 2, 6, 24
#         24 24 12  4
        
        return self.sol2(nums)
    
    # O(N), O(N)
    def sol1(self, nums):
        
        l = len(nums)
        
        pre = [1] * (l + 1)
        for i in range(l):
            pre[i + 1] = pre[i] * nums[i]
        
        post = [1] * (l + 1)
        for i in range(l - 1, -1, -1):
            post[i] = post[i + 1] * nums[i]
        
        res = [1] * l
        for i in range(l):
            res[i] = pre[i] * post[i + 1]
        
        return res
        
    # O(N), O(1)
    # [1,2,3,4,5,6]
    # in-place的思想
    
    def sol2(self, nums):
        
        res = [1] * len(nums)
        
        pre_P, post_P = 1, 1
        for i in range(len(nums)):
            res[i] *= pre_P   
            pre_P *= nums[i]
        #[1,1,2,6]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post_P
            post_P *= nums[i]
        # [24, 12, 4, 1]
        return res
            
