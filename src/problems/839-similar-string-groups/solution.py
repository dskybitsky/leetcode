from typing import List


class Solution:
    def are_swap_one(self, s1: str, s2: str) -> bool:
        num_diff = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diff += 1

            if num_diff > 2:
                return False
            
        return True

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs[0])

        strs_index = set(strs)

        ans = 0

        while len(strs_index) > 0:
            strs_to_process = [strs_index.pop()]

            ans += 1

            while len(strs_to_process) > 0:
                s = strs_to_process.pop(0)
                strs_index.discard(s)

                for s1 in strs_index:
                    if self.are_swap_one(s, s1):
                        strs_to_process.append(s1)

        return ans
    

if __name__ == '__main__':
    sol = Solution()

    assert sol.numSimilarGroups(["tars", "rats", "arts", "star"]) == 2
    assert sol.numSimilarGroups(["omv", "ovm"]) == 1
    
