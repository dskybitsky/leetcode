class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n

        def getMinSum(a: int) -> int:
            a1l = max(a - index, 1)
            a1r = max(a - n + index + 1, 1)

            sl = int((a1l + a) * min(a, index + 1) / 2)
            sr = int((a1r + a) * min(a, n - index) / 2)

            return sl + sr - a
        
        left = 0
        right = maxSum
        
        while right - left > 1:
            mid = (left + right) // 2

            minSum = getMinSum(mid)

            if minSum > maxSum:
                right = mid
            else:
                left = mid

        return (right if getMinSum(right) <= maxSum else left) + 1


sol = Solution()

assert sol.maxValue(n = 4, index = 0, maxSum = 4) == 1
assert sol.maxValue(n = 1, index = 0, maxSum = 24) == 24
assert sol.maxValue(n = 8, index = 7, maxSum = 14) == 4
assert sol.maxValue(n = 4, index = 2, maxSum = 6) == 2
assert sol.maxValue(n = 6, index = 1,  maxSum = 10) == 3

print("Ok")