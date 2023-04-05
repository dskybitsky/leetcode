import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import Dict, List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_dict = self.create_words_dict(words)

        word_len = len(words[0])
        words_len = len(words) * word_len

        ans = []

        p = 0

        chunk_words_dicts = []

        while p < len(s) - words_len:
            if p < word_len:
                chunk_words_dicts.append(self.create_words_dict(
                    self.split_string(s, p, words_len, word_len)
                ))
            else:
                self.dec_dict(chunk_words_dicts[p % word_len], s[p - word_len:p])
                self.inc_dict(chunk_words_dicts[p % word_len], s[p:p + word_len])

            if chunk_words_dicts[p % word_len] == words_dict:
                ans.append(p)
            
            p += 1

        chunk_words_dict = self.create_words_dict(
            self.split_string(s, p, words_len, word_len)
        )

        if chunk_words_dict == words_dict:
            ans.append(p)

        return ans
    
    def inc_dict(self, dict: Dict[str, int], member: str):
        dict[member] = dict[member] + 1 if member in dict else 1

    def dec_dict(self, dict: Dict[str, int], member: str):
        dict[member] -= 1

        if dict[member] == 0:
            dict.pop(member)

    def split_string(self, s: str, offset: int, length: int, chunk_size: int) -> List[str]:
        return [s[i:i+chunk_size] for i in range(offset, offset + length, chunk_size)]
    
    def create_words_dict(self, words: List[str]) -> Dict[str, int]:
        words_dict = {}

        for word in words:
            words_dict[word] = words_dict[word] + 1 if word in words_dict else 1

        return words_dict


###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_findSubstring(self):
        solution = Solution()

        # self.assertEqual(solution.findSubstring("a", ["a","a"]), [])

        # self.assertEqual(solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]), [8])

        # self.assertEqual(
        #     solution.findSubstring(
        #         "lingmindraboofooowingdingbarrwingmonkeypoundcake", 
        #         ["fooo","barr","wing","ding","wing"]
        #     ),
        #     [13]
        # )

        self.assertEqual(solution.findSubstring("barfoothefoobarman", ["foo","bar"]), [0, 9])
        self.assertEqual(solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]), [])
        self.assertEqual(solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]), [6, 9, 12])

if __name__ == '__main__':
    unittest.main()
