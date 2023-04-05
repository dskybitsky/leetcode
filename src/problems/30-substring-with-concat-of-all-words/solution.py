import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_map = self.create_words_map(words)

        words_letters_map = {}

        for word in words:
            for letter in word:
                words_letters_map[letter] = (
                    words_letters_map[letter] + 1 if letter in words_letters_map else 1
                )

        word_len = len(words[0])
        words_len = len(words) * word_len

        chunk_letters_map = {}

        if len(s)< words_len:
            return []

        for i in range(0, words_len):
            chunk_letters_map[s[i]] = (
                chunk_letters_map[s[i]] + 1 if s[i] in chunk_letters_map else 1
            )

        ans = []

        p = 0

        while p < len(s) - words_len:
            if chunk_letters_map == words_letters_map:
                chunk_words_map = self.create_words_map(
                    self.split_string(s[p:p + words_len], word_len)
                )

                if chunk_words_map == words_map:
                    ans.append(p)

            chunk_letters_map[s[p]] -= 1

            if chunk_letters_map[s[p]] == 0:
                chunk_letters_map.pop(s[p])

            next_letter = s[p + words_len]

            chunk_letters_map[next_letter] = (
                chunk_letters_map[next_letter] + 1 if next_letter in chunk_letters_map else 1
            )   

            p += 1

        if chunk_letters_map == words_letters_map:
            chunk_words_map = self.create_words_map(
                self.split_string(s[p:p + words_len], word_len)
            )

            if chunk_words_map == words_map:
                ans.append(p)

        return ans
    
    def split_string(self, s: str, chunk_size: int) -> List[str]:
        return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]
    
    def create_words_map(self, words: List[str]) -> dict[str, int]:
        words_map = {}

        for word in words:
            words_map[word] = words_map[word] + 1 if word in words_map else 1

        return words_map


###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_findSubstring(self):
        solution = Solution()

        self.assertEqual(solution.findSubstring("a", ["a","a"]), [])

        self.assertEqual(solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]), [8])

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
