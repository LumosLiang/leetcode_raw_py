class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #         [1,2,3,4]
        #         1, 2, 6, 24
        #         24 24 12  4
        #        思路变化： 1, 比较直接：分别算每一位的前缀积，后缀积（包含自己） -> 2, 分别算每一位的前后缀积, 不包含自己， -> 3, 一块儿算。
        
        return self.sol1(nums)
    
    # O(N), O(N)
    def sol1(self, nums):
        
        l = len(nums)
        # 直接算每一位的前后缀积
        pre = [1] * l
        for i in range(1, l):
            pre[i] = pre[i - 1] * nums[i - 1]
        print(pre)
        post = [1] * l
        for i in range(l - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        print(post)
        res = [1] * l
        for i in range(l):
            res[i] = pre[i] * post[i]
        
        return res
        
    # O(N), O(1)
    # [1,2,3,4,5,6]
    # 改进了以上的算法，放在一个里面算。
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
            


    def sol3(self, nums: List[int]) -> List[int]:

        #         [1,2,3,4]

        #     --> [_,1,2,6]
        #     --> [24,12,4,_]

    
        res, pre, l = [], 1, len(nums)
        
        for i in range(l):
            res.append(pre)
            pre = pre * nums[i]
        
        pre = 1
        
        for i in range(l - 1, -1, -1):
            res[i] *= pre
            pre = pre * nums[i]
        
        return res
