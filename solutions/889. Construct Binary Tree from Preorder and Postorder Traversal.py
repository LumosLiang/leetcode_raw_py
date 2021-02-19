# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        
        if not pre: return None
        if len(pre) == 1: return TreeNode(pre[0])
        
        root = TreeNode(pre[0])
        idx_left_r = post.index(pre[1])
        idx_right_r = pre.index(post[-2])
        
        if idx_left_r == len(post) - 2:
            root.left = self.constructFromPrePost(pre[1:], post[:-1])
            root.right = None
        elif idx_right_r == 1:
            root.left = None
            root.right = self.constructFromPrePost(pre[idx_right_r:], post[:-1])
        else:
            root.left = self.constructFromPrePost(pre[1:idx_right_r], post[:idx_left_r + 1])
            root.right = self.constructFromPrePost(pre[idx_right_r:], post[idx_left_r + 1:-1])
​
        return root
