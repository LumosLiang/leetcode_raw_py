class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        return self.sol2(nums, k)
    
    # incorrect, must TLE, O(k * N), worst O(N * N)
    def sol1(self, nums: List[int], k: int):
        
        l, r = 0, 0
        res = []
        nums += [float(-inf)]
        
        while r < len(nums):
            
            if r - l == k:
                res.append(max(nums[l:r]))
                l += 1    
            r += 1
        
        return res
            
    
    # so question is how we make this part "max(nums[l:r])" less than O(k)
    # first came to mind is heap
    
        # 第一想法是：(N - k) * klogk，始终维护一个k的heap，然后在每一步从heap里面弹出“对应的最左边的”。
        # 但是这样花费很多时间，有可能需要弹出整个heap才能找到，而且还要再把剩下的不需要弹出的加回去
        
        # 是否有必要每次都弹出最左边的？
        # 答案是没有必要，只有当heap顶端等于最左边的，弹出就行了，剩下的留着也可以。因为我们只是要最大
        
        # ！以上再次错了，如果只是当heap的顶端等于最左边，那么就会忽略掉之前存在的相同值的element，
        # 但是如果仅仅是根据值相等来弹出，那么又会把后面的可能性也一块儿弹出。这是不能接受的。
        # 所以这里不能采用值相等的标准，这里需要通过下标判断
            # 如果处于顶端的下标是 小于等于左边界的：那么就需要弹出。
            # 如果是大于左边界的，那么久暂时保留。
        
    # Nlogk
    def sol2(self, nums: List[int], k: int):
        
        l = 0
        res = []
        heap = []
        
        for r, v in enumerate(nums):  
            heapq.heappush(heap, [-v, r])
            if r - l + 1 == k:
                res.append(-heap[0][0])
                while heap and heap[0][1] <= l:
                    heapq.heappop(heap)
                l += 1
            
        return res       
    
#         if k == 1: return nums
#         heap = [(-val, i) for i, val in enumerate(nums[:k])]
#         heapq.heapify(heap)
#         res = [-heap[0][0]]

#         for i in range(k, len(nums)):
#             while heap[0][1] <= i - k: 
#                 heapq.heappop(heap)
                
#             heapq.heappush(heap, (-nums[i], i))
#             res.append(-heap[0][0])
#             print(heap)
       
    
    # deque
    # 为什么要用deque，首先来保持弹出和放入都是O(1)，更快了
    # 因为我们只关注最大，所以在 “k范围内，我们可以做单调队列”，小的数我们可以直接扔掉
    # 怎么弹出呢？
    # 我们就是不断的弹出nums[l], 
    # - 如果nums[l]就是当前队列的最大值，就弹出，
    # - 如果不是，就不管：这里只有一种可能就是最大值，或者已经在先前的处理被弹出过了
    
    def sol3(self, nums: List[int], k: int):
        l = 0
        res = []
        # nums += [float(-inf)]
        dq = collections.deque()
        
        for r, v in enumerate(nums):  
                     
            # make it like a heap, but in the same time, pop the not necessary elements.
            while dq and dq[-1] < v:
                dq.pop()
            dq.append(v)
            
            # when reach the right bound
            if r - l == k - 1:
                
                # append the current largest number
                res.append(dq[0])
                
                # if the left is the largest, then we need to pop it right now
                if dq and nums[l] == dq[0]:
                    dq.popleft()
                
                l += 1

            
        return res  
