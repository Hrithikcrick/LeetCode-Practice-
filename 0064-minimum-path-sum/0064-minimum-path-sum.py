class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[0 for _ in range(n)] for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j ==0:
                    dp[i][j]=grid[i][j]
                    continue
                up=float('inf')
                down=float('inf')
                if i > 0:
                    up=dp[i-1][j]
                if j > 0:
                    down=dp[i][j-1]
                dp[i][j]=grid[i][j] + min(up,down)
        return dp[m-1][n-1]   