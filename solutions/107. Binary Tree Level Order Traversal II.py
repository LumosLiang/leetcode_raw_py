# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.res = []
        
        def helper(root, level):
            if root:
                if len(self.res) < level + 1:
                    self.res.insert(0, [])
                self.res[-(level + 1)].append(root.val)
                helper(root.left, level + 1)
                helper(root.right, level + 1)
        
        helper(root, 0)
        return self.res
    
    def levelOrderBottom1(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        res = [[root.val]]
        q = [root]
        
        while q:
            temp = []
            temp_val = []
            while q:
                node = q.pop(0)
                if node.left:
                    temp.append(node.left)
                    temp_val.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    temp_val.append(node.right.val)
            if temp_val:
                res.append(temp_val)
            q = temp
        return res[::-1]
