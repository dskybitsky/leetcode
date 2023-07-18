class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n > 0:
            res += n % 2
            n = n // 2

        return res


sol = Solution()

assert sol.hammingWeight(1) == 1
assert sol.hammingWeight(2) == 1
assert sol.hammingWeight(3) == 2
assert sol.hammingWeight(7) == 3