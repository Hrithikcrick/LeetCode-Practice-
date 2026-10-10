class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMost(k):

            if k < 0:
                return 0

            left = 0
            count = 0
            arr_len = 0

            for right in range(len(nums)):

                if nums[right] % 2 == 1:
                    count += 1

                while count > k:

                    if nums[left] % 2 == 1:
                        count -= 1

                    left += 1

                arr_len += right - left + 1

            return arr_len

        return atMost(k) - atMost(k - 1)