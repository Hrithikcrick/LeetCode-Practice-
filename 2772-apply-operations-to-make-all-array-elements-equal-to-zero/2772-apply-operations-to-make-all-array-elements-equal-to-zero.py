class Solution:
    def checkArray(self, nums, k):
        n = len(nums)

        expire = [0] * (n + 1)
        current_effect = 0

        for i in range(n):

            current_effect -= expire[i]

            x = nums[i] - current_effect

            if x < 0:
                return False

            if x > 0:

                if i + k > n:
                    return False

                current_effect += x

                expire[i + k] += x

        return True


        