class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        # 看一看输入，不可能是求所有subarray 再相加
        # 至多应该是 O(N^2)的方法。
        return self.optimal(arr)
    
    # brute force
    def bruteforce(self, arr):
        
        res = arr[0]
        
        for i in range(1, len(arr)):
            curr_min = arr[i]
            for j in range(i, -1, -1):
                curr_min = min(curr_min, arr[j])
                res += curr_min
        
        return res % (1000000007)
    
     # insights
     # 降到O(N)
     # 像是84那一题一样
    def optimal(self, arr):
        
        arr.append(0)
        stack = [-1]
        res = 0
        
        # 构造单调递增栈
        for idx, val in enumerate(arr):
            
            while stack and arr[stack[-1]] > val:
                curr = stack.pop()
                h = arr[curr]
                w = idx - stack[-1] - 1
                # res += h * w
                # res += h * (idx - curr - 1) * (curr - stack[-1] - 1) 
                
                res += h * (curr - stack[-1]) * (idx - curr)
                
            stack.append(idx)
        
        return res % (1000000007)
        
​
