class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        num=set(nums)
        if target in num:
            return True
        return False