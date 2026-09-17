class Solution:
    def countRotations(self, s: str, k: int) -> int:

        rotated_arr = []
        cnt = 0

        for i in range(len(s)):

            new_s = s[i:] + s[:i]

            rotated_arr.append(new_s)

        for num in rotated_arr:

            adj = 0

            for j in range(len(num) - 1):

                if num[j] == num[j + 1]:
                    adj += 1

            if adj == k:
                cnt += 1

        return cnt