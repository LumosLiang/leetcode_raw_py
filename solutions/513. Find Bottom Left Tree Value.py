class Solution:
    def findBottomLeftValue(self, root: 'TreeNode') -> 'int':
        queue = [root]
        while queue:
            node = queue.pop(0)
            res = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return res
