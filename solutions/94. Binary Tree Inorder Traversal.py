class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []
        ans, stack = [], []
        
        while len(stack) != 0 or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                ans.append(node.val)
                root = node.right
        return ans
                
