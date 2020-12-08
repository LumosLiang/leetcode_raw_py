class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if root is None: return None
​
        if root.val == key:
            if root.right is None:
                return root.left
​
            if root.left is None:
                return root.right
​
            if root.left and root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
​
        elif root.val > key:
             root.left = self.deleteNode(root.left, key)
        else:
             root.right = self.deleteNode(root.right, key)
​
        return root
