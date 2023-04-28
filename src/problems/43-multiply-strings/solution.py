class Solution:
    def multiply_digit(self, num: str, digit: int) -> int:
        ans = 0

        carry = 0
        mult = 1

        for c in num[::-1]:
            p1 = int(c) * digit + carry
            
            ans += (p1 % 10) * mult

            carry = p1 // 10

            mult *= 10

        ans += carry * mult

        return ans

    def multiply(self, num1: str, num2: str) -> str:
        ans = 0

        n1, n2 = len(num1), len(num2)

        mult = 1

        for c in num2[::-1]:
            ans += self.multiply_digit(num1, int(c)) * mult
            mult *= 10

        return str(ans)


if __name__ == "__main__":
    sol = Solution()

    assert sol.multiply("123", "9") == "1107"
    assert sol.multiply("2", "3") == "6"
    assert sol.multiply("123", "456") == "56088"