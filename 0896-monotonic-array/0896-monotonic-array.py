class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        p = sorted(nums)
        q = sorted(nums, reverse=True)

        if nums == p or nums == q:
            return True

        return False
        
        
                

        
        

                


        