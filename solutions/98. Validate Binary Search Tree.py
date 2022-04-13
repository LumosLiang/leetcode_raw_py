# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
​
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
​
        # recursive的做
        
        # 点，BST，真正应该比较的并不是相邻的节点，而是左边，最靠右的，和右边最靠左的。
        return self.sol2(root)
    
    # O(N), O(h)
    def sol1(self, root):
        
        def helper(root, smaller, larger):
            
            if not root: return True
            
            if smaller < root.val < larger:
                return helper(root.left, smaller, root.val) and helper(root.right, root.val, larger)
            
            return False
        
        return helper(root, float('-inf'), float('inf'))
            
    # iterative的做 才是真正的难点
    def sol2(self, root):
        
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            curr, left, right = stack.pop()
            
            if not curr: continue
            
            if left < curr.val < right:
                stack.append((curr.right, curr.val, right))
                stack.append((curr.left, left, curr.val))
            else:
                return False
        
        return True
            
            
            
        
        
