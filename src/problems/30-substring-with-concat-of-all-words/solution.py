import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_map = {}

        for word in words:
            words_map[word] = words_map[word] + 1 if word in words_map else 1

        word_len = len(words[0])

        p_1, p_2 = 0, 0

        ans = []

        while p_1 < len(s):
            s_chunk = s[p_1:p_1 + word_len]

            if s_chunk in words_map:
                words_map_cp = words_map.copy()

                p_2 = p_1

                while p_2 < len(s):
                    s_chunk_2 = s[p_2:p_2 + word_len]

                    if s_chunk_2 in words_map_cp:
                        words_map_cp[s_chunk_2] -= 1

                        if words_map_cp[s_chunk_2] == 0:
                            words_map_cp.pop(s_chunk_2)

                        if len(words_map_cp) == 0:
                            ans.append(p_1)
                            break

                        p_2 += word_len
                    else:
                        break;

            p_1 += 1

        return ans

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_findSubstring(self):
        solution = Solution()

        self.assertEqual(
            solution.findSubstring(
                "lingmindraboofooowingdingbarrwingmonkeypoundcake", 
                ["fooo","barr","wing","ding","wing"]
            ),
            [13]
        )

        self.assertEqual(solution.findSubstring("barfoothefoobarman", ["foo","bar"]), [0, 9])
        self.assertEqual(solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]), [])
        self.assertEqual(solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]), [6, 9, 12])

if __name__ == '__main__':
    unittest.main()
