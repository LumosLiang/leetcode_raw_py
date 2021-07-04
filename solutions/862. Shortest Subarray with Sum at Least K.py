class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        
        res = float('inf')
        dq = collections.deque([[0, 0]])
        csum = 0
        for i, v in enumerate(A):
            csum += v
            while dq and csum - dq[0][1] >= K:
                res = min(i - dq.popleft()[0] + 1, res)
            while dq and csum <= dq[-1][1]:
                dq.pop()
            dq.append([i + 1, csum])
            
        return res if res != float('inf') else -1
​
            
