class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        values = []
        def getValues(root):
            if not root:
                return
            values.append(root.val)
            if root.left:
                getValues(root.left)
            if root.right:
                getValues(root.right)
        getValues(root)
        values = sorted(set(values))
        if len(values) > 1:
            return values[1]
        return -1
