class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        dp=[[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[n-1][j]=triangle[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                down=dp[i+1][j]
                right=dp[i+1][j+1]
                dp[i][j]=triangle[i][j]+min(down,right)
        return dp[0][0]
        