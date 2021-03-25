class Solution:
    def splitListToParts(self, root, k):
        
        if root is None: return k * [None]
        
        curr = root
        res, stack = [],[]
        
        l = 0
        while curr:
            curr = curr.next
            l += 1
        
        while k != 0:
            stack.append(l // k)
            l -= l // k
            k -= 1
        
        curr = root
        while stack:
            temp = stack.pop()
            head = curr
            
            if temp == 0:
                res.append(None)
                continue
                
            while temp > 1:
                curr = curr.next
                temp -= 1
            
            nxt = curr.next
            curr.next = None
            res.append(head)
            curr = nxt
        
        return res
