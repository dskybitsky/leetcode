class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        snum = str(num)

        for sdigit in snum:
            ans += int(sdigit)

            if ans > 9:
                ans -= 9

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.addDigits(38) == 2
    assert sol.addDigits(0) == 0