class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atmost(k):
            left=0
            freq={}
            maxi=0
            for right in range(len(nums)):
                freq[nums[right]]=freq.get(nums[right],0)+1
                while len(freq)>k:
                    freq[nums[left]]-=1
                    if freq[nums[left]]==0:
                        del freq[nums[left]]
                    left+=1
                maxi+=right-left+1
            return maxi
        return atmost(k)-atmost(k-1)

        