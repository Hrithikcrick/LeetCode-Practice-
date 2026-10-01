class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:

        
        end_at = [[] for _ in range(n + 1)]

        for start, end, tip in rides:
            end_at[end].append((start, tip))

       
        dp = [0] * (n + 1)

        for x in range(1, n + 1):

            dp[x] = dp[x - 1]

            
            for start, tip in end_at[x]:

                earning = x - start + tip

                dp[x] = max(
                    dp[x],
                    dp[start] + earning
                )

        return dp[n]
        