class Solution:
    def nextLargerNodes(self, head):
        
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
            
        s, res = [],[0] * len(lst)
        
        for i in range(len(lst) - 1, -1, -1):
            while s and s[-1] <= lst[i]:
                s.pop()
            if s: res[i] = s[-1]
            s.append(lst[i])
        
        return res   
