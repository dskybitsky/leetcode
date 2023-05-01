from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        n = 0
        total = 0
        min_sal = None
        max_sal = None

        for sal in salary:
            n += 1
            total += sal

            if min_sal is None or sal < min_sal:
                min_sal = sal
            
            if max_sal is None or sal > max_sal:
                max_sal = sal

        return (total - min_sal - max_sal) / (n - 2)


if __name__ == "__main__":
    sol = Solution()

    assert sol.average([4000, 3000, 1000, 2000]) == 2500.0