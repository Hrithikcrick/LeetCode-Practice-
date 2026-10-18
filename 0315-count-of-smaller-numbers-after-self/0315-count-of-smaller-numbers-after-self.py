
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:

        # Step 1: Coordinate compression
        rank = {x: i + 1 for i, x in enumerate(sorted(set(nums)))}

        # Step 2: Create Fenwick Tree
        bit = [0] * (len(rank) + 1)

        # Step 3: Count previously inserted smaller values
        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        # Step 4: Insert current value
        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        # Step 5: Process array right to left
        ans = [0] * len(nums)

        for j in range(len(nums) - 1, -1, -1):
            r = rank[nums[j]]
            ans[j] = query(r - 1)
            update(r)

        return ans
