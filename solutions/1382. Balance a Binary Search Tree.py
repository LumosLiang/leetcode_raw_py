# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nodes, stack = [], []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                nodes.append(temp.val)
                root = temp.right
                
        def generateTree(l, r):
            
            if l > r: return None
​
            mid = l + (r - l) // 2
            root = TreeNode(nodes[mid])
            root.left = generateTree(l, mid - 1)
            root.right = generateTree(mid + 1,r)
            
            return root
        
        return generateTree(0, len(nodes) - 1)
