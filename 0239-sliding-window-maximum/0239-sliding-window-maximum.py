class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq=deque()
        ans=[]
        for i in range(len(nums)):
            while dq and dq[0]<i-k+1:
                dq.popleft()
            while dq and nums[i]>=nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >=k-1:
                ans.append(nums[dq[0]])
        return ans
        