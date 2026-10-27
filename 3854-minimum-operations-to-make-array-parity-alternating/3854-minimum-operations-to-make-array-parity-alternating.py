from typing import List

class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 0]

        smallest = min(nums)
        largest = max(nums)
        ans = []

        for first in [0, 1]:
            count = 0
            new_min = float('inf')
            new_max = float('-inf')

            for i in range(len(nums)):
                target = (first + i) % 2
                x = nums[i]

                if x % 2 != target:
                    count += 1

                    if x == smallest:
                        x += 1
                    elif x == largest:
                        x -= 1

                new_min = min(new_min, x)
                new_max = max(new_max, x)

            p = max(1, new_max - new_min)
            ans.append([count, p])

        return min(ans)