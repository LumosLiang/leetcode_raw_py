# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None: return None
        
        lst = collections.Counter()
        def inorder(root):
            if root.left: inorder(root.left)
            lst[root.val] += 1
            if root.right: inorder(root.right)
        inorder(root)
        print(lst)
        most = lst.most_common()[0][1]
        return [k for k, v in lst.items() if v == most]
