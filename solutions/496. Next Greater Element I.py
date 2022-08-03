class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return self.sol2(nums1, nums2)
        
    def sol1(self, nums1: List[int], nums2: List[int]):
        s = []
        table = collections.defaultdict()
        
        for j in range(len(nums2)-1, -1, -1):
            while s and s[-1] < nums2[j]:
                s.pop()
            if not s: table[nums2[j]] = -1
            else: table[nums2[j]] = s[-1]
            s.append(nums2[j])
        
        res = []
        for n in nums1:
            if n in table: res.append(table[n])
        return res
        
    
        # right to left
        # compare with lastseen biggest numbers with the curr one
            # if lastseen > curr, then it is the last one, then put itself into stack.
            # if lastseen < curr, pop lastseen till we saw a larger one
            # if stack is empty or we pop the stack till empty, then no greater, set to -1, append it
        # stack's function:
            # store the closest(Next) larger number
            # and store them in the small to large order(top to bottom)
        
    def sol2(self, nums1, nums2):
        s = []
        table = collections.defaultdict()
        
        for i, val in enumerate(nums2):
            while s and nums2[s[-1]] < val:
                j = s.pop()
                table[nums2[j]] = val
            s.append(i)
        
        res = []
        for n in nums1:
            if n in table: res.append(table[n])
            else: res.append(-1)
        return res
