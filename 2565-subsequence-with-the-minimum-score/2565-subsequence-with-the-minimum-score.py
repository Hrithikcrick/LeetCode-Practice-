class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        left = [-1] * (m + 1)
        left[0] = -1

        j = 0
        for i in range(n):
            if j < m and s[i] == t[j]:
                j += 1
                left[j] = i

        if j == m:
            return 0

        ans = m - j
        k = j
        r = m - 1

        for i in range(n - 1, -1, -1):
            while k > 0 and left[k] >= i:
                k -= 1

            if r >= 0 and s[i] == t[r]:
                ans = min(ans, r - k)
                r -= 1

        return ans
        