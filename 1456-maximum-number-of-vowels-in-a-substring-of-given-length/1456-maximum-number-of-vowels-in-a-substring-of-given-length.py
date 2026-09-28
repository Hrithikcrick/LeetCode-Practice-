class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set("aeiou")

        left = 0
        count = 0
        maxi = 0

        for right in range(len(s)):

            # Add right character
            if s[right] in vowels:
                count += 1

            # Complete window created
            if right - left + 1 == k:

                # calculate answer
                maxi = max(maxi, count)

                # remove left character
                if s[left] in vowels:
                    count -= 1

                # move left for next window
                left += 1

        return maxi