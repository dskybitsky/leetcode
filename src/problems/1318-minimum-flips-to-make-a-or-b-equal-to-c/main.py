class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a > 0 or b > 0 or c > 0:
            am = a % 2
            bm = b % 2
            cm = c % 2

            if cm == 0:
                if am == 1:
                    flips += 1
                if bm == 1:
                    flips += 1
            else:
                if am == 0 and bm == 0:
                    flips += 1

            a = a // 2
            b = b // 2
            c = c // 2

        return flips


sol = Solution()

assert sol.minFlips(2, 6, 5) == 3
assert sol.minFlips(4, 2, 7) == 1
assert sol.minFlips(1, 2, 3) == 0
assert sol.minFlips(7, 7, 7) == 0
assert sol.minFlips(8, 3, 5) == 3

print("Ok")