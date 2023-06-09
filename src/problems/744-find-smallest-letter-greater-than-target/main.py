from typing import List
import bisect

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        pos = bisect.bisect_right(letters, target)

        if pos < n:
            return letters[pos]

        return letters[0]


sol = Solution()

assert sol.nextGreatestLetter(letters = ["c","f","j"], target = "a") == "c"
assert sol.nextGreatestLetter(letters = ["c","f","j"], target = "c") == "f"
assert sol.nextGreatestLetter(letters = ["x","x","y","y"], target = "z") == "x"

print("Ok")