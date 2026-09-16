class Solution:
    def reverseWords(self, s: str) -> str:

        store = []

        ans = ""

        # Build and store words
        for ch in s:

            if ch == ' ':

                if ans:
                    store.append(ans)
                    ans = ""

            else:
                ans += ch

        # Store the last word
        if ans:
            store.append(ans)

        # Build result in reverse order
        res = []

        for i in range(len(store) - 1, -1, -1):
            res.append(store[i])

        return ' '.join(res)
        