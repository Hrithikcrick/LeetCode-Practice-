class Solution:
    def maxOperations(self, nums: list[int]) -> int:

        n = len(nums)

        if n < 2:
            return 0

        def run(left, right, target):

            # Number of elements remaining
            length = right - left + 1

            # 0 or 1 element left:
            # no more pair can be removed
            if length < 2:
                return 0

            # prev[l] stores answer for the interval
            # of length current_len - 2 starting at l
            prev = [0] * (n + 2)

            # If remaining interval length is even:
            # start building from length 2.
            #
            # If remaining interval length is odd:
            # base is length 1, so first useful length is 3.
            if length % 2 == 0:
                current_len = 2
            else:
                current_len = 3

            while current_len <= length:

                curr = [0] * (n + 2)

                last_start = right - current_len + 1

                for l in range(left, last_start + 1):

                    r = l + current_len - 1

                    ans = 0

                    # OPTION 1:
                    # remove first two
                    if nums[l] + nums[l + 1] == target:
                        ans = max(
                            ans,
                            1 + prev[l + 2]
                        )

                    # OPTION 2:
                    # remove last two
                    if nums[r - 1] + nums[r] == target:
                        ans = max(
                            ans,
                            1 + prev[l]
                        )

                    # OPTION 3:
                    # remove first and last
                    if nums[l] + nums[r] == target:
                        ans = max(
                            ans,
                            1 + prev[l + 1]
                        )

                    curr[l] = ans

                prev = curr
                current_len += 2

            return prev[left]

        # First operation decides the target score

        # 1. first two
        ans1 = 1 + run(
            2,
            n - 1,
            nums[0] + nums[1]
        )

        # 2. last two
        ans2 = 1 + run(
            0,
            n - 3,
            nums[n - 2] + nums[n - 1]
        )

        # 3. first + last
        ans3 = 1 + run(
            1,
            n - 2,
            nums[0] + nums[n - 1]
        )

        return max(ans1, ans2, ans3)