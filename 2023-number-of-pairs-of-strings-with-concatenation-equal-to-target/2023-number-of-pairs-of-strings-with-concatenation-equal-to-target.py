class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        s=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    n=nums[i]+nums[j]
                    if n==target:
                        s.append((i,j))
        return len(s)
        