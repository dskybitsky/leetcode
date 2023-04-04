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
        words_letters_map = {}

        for word in words:
            words_map[word] = words_map[word] + 1 if word in words_map else 1
            
            for letter in word:
                words_letters_map[letter] = (
                    words_letters_map[letter] + 1 if letter in words_letters_map else 1
                )

        word_len = len(words[0])
        words_len = len(words) * word_len

        chunk_letters_map = {}

        for i in range(0, words_len):
            chunk_letters_map[s[i]] = (
                chunk_letters_map[s[i]] + 1 if s[i] in chunk_letters_map else 1
            )

        ans = []

        p = 1

        while p < len(s) - words_len:
            if chunk_letters_map == words_letters_map:
                chunk_words = [ s[i:i+word_len] for i in range(p - 1, words_len, word_len) ]

                chunk_words_map = {}

                for chunk_word in chunk_words:
                    chunk_words_map[chunk_word] = chunk_words_map[chunk_word] + 1 if chunk_word in chunk_words_map else 1

                if (chunk_words_map == words_map):
                    ans.append(p - 1)

            chunk_letters_map[s[p - 1]] -= 1

            if chunk_letters_map[s[p - 1]] == 0:
                chunk_letters_map.pop(s[p - 1])
            
            chunk_letters_map[s[p + words_len - 1]] = (
                chunk_letters_map[s[p + words_len - 1]] + 1
                if s[p + words_len - 1] in chunk_letters_map else 1
            )                               

            p += 1

        return ans

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_findSubstring(self):
        solution = Solution()

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
