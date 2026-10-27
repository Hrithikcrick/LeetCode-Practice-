class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 0]

        merunavilo = nums
        ans = []
        mn = min(nums)
        mx = max(nums)

        for first in [0, 1]:
            count = 0
            mini = float('inf')
            maxi = float('-inf')

            for i in range(len(nums)):
                target = (first + i) % 2
                x = nums[i]

                if x % 2 != target:
                    count += 1

                    if x == mn:
                        x += 1
                    elif x == mx:
                        x -= 1

                mini = min(mini, x)
                maxi = max(maxi, x)

            p = max(1, maxi - mini)
            ans.append([count, p])

        return min(ans)