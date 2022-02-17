public class Solution {
    public int OrangesRotting(int[][] grid)
    {
​
        // first loop, to generate a q and count how many oranges totally.
​
        int m = grid.Length, n = grid[0].Length, res = 0, count = 0;
        int[] DIR = new int[] { 0, 1, 0, -1, 0 };
        Queue<int[]> q = new Queue<int[]>();
​
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] != 0)
                {
                    if (grid[i][j] == 2)
                    {
                        grid[i][j] = -1; // mark as processed
                        q.Enqueue(new int[] { i, j });
                    }
                    else count += 1;
​
                }
            }
        }
        
        if (q.Count == 0 && count == 0) return 0;
​
        // second, BFS, start from rotten one, make all fresh organge rotten.
        while (q.Count != 0)
        {
            Queue<int[]> temp = new Queue<int[]>();
            while (q.Count != 0)
            {
                var item = q.Dequeue();
                int r = item[0], c = item[1];
                for (int k = 0; k < 4; k++)
                {
                    int nr = r + DIR[k], nc = c + DIR[k + 1];
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0 || grid[nr][nc] == -1) continue;
                    grid[nr][nc] = -1;
                    count -= 1;
                    temp.Enqueue(new int[] { nr, nc });
                }
            }
            q = temp;
            res += 1;
        }
​
        if (count == 0) return res - 1;
        else return -1;
    }
}
