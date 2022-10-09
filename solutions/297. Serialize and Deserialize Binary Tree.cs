/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
​
// DFS, BFS
​
public class Codec {
​
    // Encodes a tree to a single string.
    public string serialize(TreeNode root) {
        
        if(root == null) return "";
        
        string res = "";
        
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        
        while(q.Count != 0)
        {
            var temp = new Queue<TreeNode>();
            while(q.Count != 0)
            {
                var curr = q.Dequeue();
                if(curr == null)
                {
                    res += "#,";
                    continue;
                }
                res += curr.val.ToString() + ",";
                temp.Enqueue(curr.left);
                temp.Enqueue(curr.right);
            }
            q= temp;
        }
        return res;
        
    }
​
    // Decodes your encoded data to tree.
    public TreeNode deserialize(string data) {
        
        if(data == "" || data[0] == '#') return null;
        data.TrimEnd(',');
        var dataArray = data.Split(',');
        var root = new TreeNode(Int32.Parse(dataArray[0]));
        
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        int i = 1;
        
        while(q.Count != 0)
        {
            var curr = q.Dequeue();
            if(dataArray[i] != "#")
            {
                curr.left = new TreeNode(Int32.Parse(dataArray[i]));
                q.Enqueue(curr.left);
            }
            i++;
            if(dataArray[i] != "#")
            {
                curr.right = new TreeNode(Int32.Parse(dataArray[i]));
                q.Enqueue(curr.right);
            }
            i++;
        }
        
        return root;
    }
}
​
// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
