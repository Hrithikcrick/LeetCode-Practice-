class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for t in range(coin,amount+1):
                dp[t]=min(dp[t],1+dp[t-coin])
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]