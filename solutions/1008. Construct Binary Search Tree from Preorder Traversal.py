class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        if not preorder: return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        # find the idx
        idx = 0
        for i in range(1, len(preorder)):
            if preorder[i] > root.val:
                idx = i
                break
        
        if idx == 1:
            root.left = None
            root.right = self.bstFromPreorder(preorder[idx:])
        elif idx == 0:
            root.left = self.bstFromPreorder(preorder[1:])
            root.right = None
        else:
            root.left = self.bstFromPreorder(preorder[1:idx])
            root.right = self.bstFromPreorder(preorder[idx:]) 
        return root
