
class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()

        total = 0
        ans = 0

        for x in reversed(satisfaction):
            total += x

            if total <= 0:
                break

            ans += total

        return ans

        