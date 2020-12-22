# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def traverseBST(root):
            if root is None: return []
            ans, stack = [], []
​
            while len(stack) != 0 or root is not None:
                if root is not None:
                    stack.append(root)
                    root = root.left
                else:
                    node = stack.pop()
                    ans.append(node.val)
                    root = node.right
            return ans
        
        return sorted(traverseBST(root1) + traverseBST(root2))
