# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def isSameTreeRecur(self, p:TreeNode, q:TreeNode):
        if not p and not q: return True
​
        if not p or not q: return False
​
        if p.val != q.val: return False
​
        return self.isSameTreeRecur(p.left, q.left) and self.isSameTreeRecur(p.right, q.right)
​
    def isSameTreeBFS(self, p:TreeNode, q:TreeNode):
        
        q = collections.deque([[p,q]])
​
        while q:
​
            n1, n2 = q.popleft()
            if not n1 and not n2: continue
            if not n1 or not n2: return False
            if n1.val != n2.val: return False
            q.append([n1.left, n2.left])
            q.append([n1.right, n2.right])
​
        return True
​
    def isSameTreeDFS(self, p:TreeNode, q:TreeNode):
​
        stack = [(p, q)]
​
        while stack:
            t1, t2 = stack.pop()
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            if t1.val != t2.val: return False
            stack.append((t1.right,t2.right))
            stack.append((t1.left,t2.left))
​
        return True
