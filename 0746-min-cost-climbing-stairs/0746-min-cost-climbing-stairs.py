class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [-1] * (n + 1)

        def solve(i):
            if i <= 1:
                return 0

            if dp[i] != -1:
                return dp[i]

            one_jump = solve(i - 1) + cost[i - 1]
            two_jump = solve(i - 2) + cost[i - 2]

            dp[i] = min(one_jump, two_jump)

            return dp[i]

        return solve(n)

        