
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        dig = n

        while dig:
            if dig < 10:
                if dig % t == 0:
                    return n
            else:
                f = dig % 10
                dig = dig // 10
                l = dig % 10

                if (l * f) % t == 0:
                    return n

            n += 1
            dig = n
