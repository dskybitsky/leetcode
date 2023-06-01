class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        left = 0
        right = n - 1

        left_n = 0
        right_n = 0

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            left_n += 1

            right -= 1
            right_n += 1

        return left_n == right_n
    

sol = Solution()

assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
assert sol.isPalindrome("race a car") is False
assert sol.isPalindrome("") is True