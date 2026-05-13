class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        res = 0

        while x != 0:
            num = int(x % 10)

            if x < 0 and num > 0:
                num -= 10

            x = int(x / 10)

            if (res > MAX_INT // 10 or (res == MAX_INT // 10 and num >= MAX_INT % 10)):
                return 0
            if (res < MIN_INT / 10 or (res == MIN_INT / 10 and num <= MIN_INT % 10)):
                return 0

            res = res * 10 + num

        return res    