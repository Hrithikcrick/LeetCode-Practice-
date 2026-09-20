class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        arr1=nums[:n-1]
        arr2=nums[1:]
        def solve(arr):
            n=len(arr)
            if n==1:
                return arr[0]
            dp=[0]*n
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])
            for i in range(2,n):
                take=arr[i]+dp[i-2]
                skip=dp[i-1]
                dp[i]=max(take,skip)
            return dp[n-1]
        case1=solve(arr1)
        case2=solve(arr2)
        return max(case1,case2)

