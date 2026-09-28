class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set("aeiou")

        left = 0
        count = 0
        max_count = 0

        for right in range(len(s)):

            # 1. ADD the new character
            if s[right] in vowels:
                count += 1

            # 2. If window becomes bigger than k,
            # REMOVE the left character
            if right - left + 1 > k:

                if s[left] in vowels:
                    count -= 1

                left += 1

            # 3. When window size is exactly k
            if right - left + 1 == k:
                max_count = max(max_count, count)

        return max_count
        