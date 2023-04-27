import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.floor(math.sqrt(n))


if __name__ == '__main__':
    sol = Solution()

    assert sol.bulbSwitch(6) == 2

    # ROUND 1   *   *   *   *   *   *
    # ROUND 2   *   0   *   0   *   0
    # ROUND 3   *   0   0   0   *   *
    # ROUND 4   *   0   0   *   *   *
    # ROUND 5   *   0   0   *   0   *
    # ROUND 6   *   0   0   *   0   0


    assert sol.bulbSwitch(3) == 1
    assert sol.bulbSwitch(0) == 0
    assert sol.bulbSwitch(1) == 1

