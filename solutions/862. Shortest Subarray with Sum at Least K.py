class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        # prefix sum + deque
        # sliding window + deque
        
        # 如果都是positive,那可以很轻松的用滑动窗口做出来，
        # 如果又negative，如果还要用滑动窗口的话，这里的窗口应该怎么设计？
        
        # 看到subarray，又看到sum，很容易想到前缀和的思路
        # 一个大概的思路是，我要有一个窗口，窗口中不断的放【idx, curr_prefix_sum】
        # 每放一个，其实你都可以找一遍这个窗口，然后判断有没有一个区间是 >= k的，如果有就更新
        # 那这个必然是一个O(N*N)的一个复杂度。
        
        
        # 如何降低复杂度呢？
        
            # 首先
            # 当这个滑动窗口真的满足条件的时候，我们就开始算区间长度。
            # 我们可以不断地loop，来找到最小满足条件的区间长度。当找到的时候，我们还需要前面的所有element吗？
            # 其实我们无需保留更小的，因为他们是在当前条件下，我们能找到的最小的了。下一个可能的答案如果真的存在，只会更小。
            # 所以他们是没有必要存在的。
            
            # 第二个优化
            #（比较难想一点），如果对于点i, i + 1, pref[i] > pref[i + 1], 如果将来有一点j可以满足 
            #         pref[j] - ref[i] >= k, 
            #         那么肯定
            #         pref[j] - pref[i + 1] >= k

            #         没有必要存pref[i]，因为更长，我们不需要
            
        # 所以单调队列是最好的数据结构，因为它能实现两边O（1）的操作
        
        # [-4,3,-2,8,9,-7,2,11]
        
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
            
        return res if res != float('inf') else -1
        
        
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C++JavaPython-O(N)-Using-Deque/150644
