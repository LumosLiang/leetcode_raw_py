class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def helper(l, r):
            if l == r: return None
            root = TreeNode(preorder[l])
            idx = bisect.bisect(preorder, preorder[l], l + 1, r)
            root.left = helper(l + 1, idx)
            root.right = helper(idx, r) 
            return root
        
        return helper(0, len(preorder))
    
  
   
