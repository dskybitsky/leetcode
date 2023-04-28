from typing import List


class Solution:
    def swap_characters(self, s: str, i: int, j: int) -> str:
        l = list(s)
        l[i], l[j] = l[j], l[i]
        
        return ''.join(l)

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs[0])

        strs_index = set(strs)

        ans = 0

        while len(strs_index) > 0:
            strs_to_process = [strs_index.pop()]

            ans += 1

            while len(strs_to_process) > 0:
                s = strs_to_process.pop(0)

                for i in range(n - 1):
                    for j in range(i + 1, n):
                        s1 = self.swap_characters(s, i, j)

                        if s1 in strs_index:
                            strs_to_process.append(s1)
                            strs_index.remove(s1)

        return ans
    

if __name__ == '__main__':
    sol = Solution()

    assert sol.numSimilarGroups(["tars", "rats", "arts", "star"]) == 2
    assert sol.numSimilarGroups(["omv", "ovm"]) == 1
    
