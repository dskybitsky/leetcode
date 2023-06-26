class Solution:
    def addBinary(self, a: str, b: str) -> str:
        an = len(a)
        bn = len(b)

        ia = an - 1
        ib = bn - 1

        carry = 0

        res = [0] * max(an, bn)

        ir = len(res) - 1

        while ia >= 0 or ib >= 0:
            ca = int(a[ia]) if ia >= 0 else 0
            cb = int(b[ib]) if ib >= 0 else 0

            s = ca + cb + carry

            if s == 1:
                res[ir] = 1
                carry = 0
            elif s == 2:
                carry = 1
            elif s == 3:
                res[ir] = 1
                carry = 1

            ia -= 1
            ib -= 1
            ir -= 1

        res_str = "".join(map(str, res))

        return res_str if carry == 0 else "1" + res_str


sol = Solution()

assert sol.addBinary(a = "11", b = "1") == "100"