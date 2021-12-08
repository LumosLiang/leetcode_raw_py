# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # Two node were swapped here. 
        
        # Think about this:
        # If we do the in-order traversal and iterate the array from left to right, at some place, the current node will be less than the prev node. And this could happen at most twice. 
            # If it happen once: The two adjacent nodes: prev and curr are exactly the ones we want
            
            1 -> 2 -> 4 -> 3 -> 5 -> 6
            
            # If it happen twice: Then at the first time, the prev node is the one we want; at the second time, the curr node is what we want.
            
            1 -> 5 -> 3 -> 4 -> 2 -> 6
            
        # So our job is to find that two nodes: node1, node2 by using in-order DFS. In fact, we actually do not need to care if this the first time or the second time, let's see these:
            # when curr node's val is larger than prev node's, we continue and update the prev
            # when curr node's val is smaller than prev node's, we do not need to update the prev, but just keep update node1 and node2 together. This is because, the val of nodes between node 1 and node2, include node2, must smaller than node1's. So once we find node1, we can safely do the update until node2.
            
   
        self.node1, self.node2, self.pre = None, None, TreeNode(float('-inf'))
        
        def helper(root):
            
            if not root: return
            
            helper(root.left)
            
            if root.val < self.pre.val:
                self.node1 = self.pre
                self.node2 = root
            else:
                self.pre = root
            
            helper(root.right)
        
        helper(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
        
