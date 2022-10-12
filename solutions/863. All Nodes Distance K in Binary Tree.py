# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.res = []
        self.DFS_sol(root, target, k)
        return self.res
        
    # O(N), O(N)
    def graph_sol(self, root: TreeNode, target: TreeNode, k: int):
        conn = collections.defaultdict(list)
        
        def connect(parent, child):
            # both parent and child are not empty
            if parent and child:
                # building an undirected graph representation, assign the
                # child value for the parent as the key and vice versa
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            # pre-order traversal
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
                
        connect(None, root)
        
        
        q = collections.deque([target.val])
        visited = set()
        visited.add(target.val)
        
        while k > 0:
            temp = collections.deque()
            while q:
                curr = q.popleft()
                for item in conn[curr]:
                    if item not in visited:
                        temp.append(item)
                        visited.add(item)
            k -= 1
            q = temp
        
        return list(q)
    
    # O(N), O(N)
    def DFS_sol(self, root: TreeNode, target: TreeNode, k: int):
        
        if not root: return
        
        isleft, dis = self.locate_target(root, target)
        
        if dis is None: return
        
        dis -= 1
        
        if dis == 0: 
            self.get_nodes(root, k)  
            return
        
        if dis == k:
            self.res.append(root.val)
    
        
        if isleft: self.get_nodes(root.right, k - dis - 1) 
        else: self.get_nodes(root.left, k - dis - 1)
​
        
        self.DFS_sol(root.left, target, k)
        self.DFS_sol(root.right, target, k)
    
    # tell me and distance between target and root
    def locate_target(self, root, target):
        
        if not root: return (False, None)
        
        if root == target: return True, 1
        
        isleft, l = self.locate_target(root.left, target)
        isleft, r = self.locate_target(root.right, target)
        
        if not l and not r: return (False, None)
        if not l: return (False, r + 1)
        if not r: return (True, l + 1)
​
    # return the nodes
    def get_nodes(self, target, k):
        
        if not target or k < 0: return
        
        if k == 0: 
            self.res.append(target.val)
            return
        
        self.get_nodes(target.left, k - 1)
        self.get_nodes(target.right, k - 1)
        
