# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # return self.solution1(root, root, root)
        
        # self.res = 0
        # self.solution2(root, -10001)
        # return self.res
        
        return self.solution4(root)
        
    def solution1(self, curr, p, lastG):
​
        if curr is None: return 0
​
        if curr.val < p.val or curr.val >= p.val and curr.val < lastG.val:
            return self.solution1(curr.left, curr, lastG) + self.solution1(curr.right, curr, lastG)
        elif curr.val >= p.val and curr.val >= lastG.val:
            return 1 + self.solution1(curr.left, curr, curr) + self.solution1(curr.right, curr, curr)
        
    def solution2(self, curr, MAX):
        if not curr: return 0
        
        if curr.val >= MAX: self.res += 1
​
        self.solution2(curr.left, max(curr.val, MAX))
        self.solution2(curr.right, max(curr.val, MAX))
​
        
    def solution3(self, curr):
​
        res, stack = 0, [(curr, -10001)]
        
        while stack:
            node, m = stack.pop()
            if not node: continue
            if node.val >= m: res += 1
​
            stack.append((node.left, max(node.val, m)))
            stack.append((node.right, max(node.val, m)))
​
        return res 
        
    def solution4(self, curr):
​
        res, q = 0, collections.deque([(curr, -10001)])
        
        while q:
            node, m = q.popleft()
            if not node: continue
            if node.val >= m: res += 1
​
            q.append((node.left, max(node.val, m)))
            q.append((node.right, max(node.val, m)))
​
        return res 
    
    
