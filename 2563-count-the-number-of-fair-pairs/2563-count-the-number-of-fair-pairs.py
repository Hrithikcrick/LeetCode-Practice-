class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def atmost(limit):
            left=0
            cnt=0
            right=len(nums)-1
            
            while left<right:
                if nums[left]+nums[right]<=limit:
                    cnt+=right-left
                    left+=1
                else:
                    right-=1
            return cnt
        return atmost(upper)-atmost(lower-1)
                        


                
        