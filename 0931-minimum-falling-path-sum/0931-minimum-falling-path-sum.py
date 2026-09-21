class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[n-1][j]=matrix[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(n):
                left_right=float('inf')
                down_right=float('inf')
                down=float('inf')
                if j > 0:
                    left_right=dp[i+1][j-1]
                if j < n - 1:
                    down_right = dp[i + 1][j + 1]
                down=dp[i+1][j]
                
                dp[i][j]=matrix[i][j]+min(left_right,down,down_right)
        return min(dp[0])

        