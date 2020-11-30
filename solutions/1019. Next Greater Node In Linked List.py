class Solution:
    def nextLargerNodes(self, head):
        pos = 0
        stack, res = [],[]
​
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            res.append(0)
            stack.append([pos, head.val])
            head = head.next
            pos += 1
            
        return res   
