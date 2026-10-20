class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if len(nums)==1:
            return 0
        nums.sort()
        curr=0
        mini=float('inf')
        left=0
        for right in range(len(nums)):
            if right-left+1==k:
                curr=max(nums[left:right+1])-min(nums[left:right+1])
                if curr<=mini:
                    mini=curr
                left+=1
        return mini
        