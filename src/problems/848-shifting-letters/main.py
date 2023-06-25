from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ord_a = ord('a')

        n = len(s)

        shift_sum = 0

        new_s = [0] * n

        for i in range(n - 1, -1, -1):
            shift_sum += shifts[i]

            new_s[i] = ((ord(s[i]) - ord_a + shift_sum) % 26) + ord_a

        return ''.join(map(chr, new_s))


sol = Solution()

assert sol.shiftingLetters(s = "abc", shifts = [3,5,9]) == "rpl"