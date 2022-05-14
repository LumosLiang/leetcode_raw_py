class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        # prefix sum + deque
        # sliding window + deque
        
        # 如果都是positive,那可以很轻松的用滑动窗口做出来，
        # 如果又negative，如果还要用滑动窗口的话，这里的窗口应该怎么设计？
        # 如何保持单调性？单调队列是一个好方法，
            # 当遇到更小的值是，弹出所有前面的，因为已经没有意义
            # 当遇到满足条件的值，弹出所有前面的不满足条件的，无需保留更小的，因为我们期望找到更好的下一个
            
        res = float('inf')
        dq = collections.deque([[-1, 0]])
        pfsum = 0
        
        for r, val in enumerate(nums):
            pfsum += val
            
            while dq and pfsum < dq[-1][1]:
                dq.pop()
            dq.append([r, pfsum])
            
            while dq and pfsum - dq[0][1] >= k:
                res = min(res, r - dq[0][0])
                dq.popleft()
​
        return res if res != float('inf') else -1
        
        
        
        
