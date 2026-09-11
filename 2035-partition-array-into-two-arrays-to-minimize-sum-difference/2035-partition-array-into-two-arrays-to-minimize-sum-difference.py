from typing import List
from itertools import combinations
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        n = len(nums) // 2
        total = sum(nums)

        left = nums[:n]
        right = nums[n:]

        ans = float("inf")

        for count in range(n + 1):

            left_sums = [sum(x) for x in combinations(left, count)]
            right_sums = sorted(sum(x) for x in combinations(right, n - count))

            for s1 in left_sums:

                target = total / 2 - s1

                i = bisect_left(right_sums, target)

                if i < len(right_sums):
                    s = s1 + right_sums[i]
                    ans = min(ans, abs(total - 2 * s))

                if i > 0:
                    s = s1 + right_sums[i - 1]
                    ans = min(ans, abs(total - 2 * s))

        return ans