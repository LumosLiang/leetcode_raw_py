# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        self.nodes = collections.defaultdict(list)
        self.traverse(root)
        return [self.nodes[node][0] for node in self.nodes if len(self.nodes[node]) > 1]
​
    def traverse(self, root):
        if not root: return "null"
        struct = "%s,%s,%s" % (str(root.val), self.traverse(root.left), self.traverse(root.right))
        self.nodes[struct].append(root)
        return 123
        
        
        
​
​
​
            
