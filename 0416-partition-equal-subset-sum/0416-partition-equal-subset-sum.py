class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        dp=[[False for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
        for i in range(1,n+1):
            for s in range(1,target+1):
                not_take=dp[i-1][s]
                take = False
                if nums[i-1]<=s:
                    take=dp[i-1][s-nums[i-1]]
                dp[i][s]=take or not_take
        return dp[n][target]
        
        