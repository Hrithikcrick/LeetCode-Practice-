class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        i = 0
        n = len(intervals)

        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]
            i += 1

            while i < n and intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                i += 1

            ans.append([start, end])

        return ans