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
                self.inc_map(words_letters_map, letter)

        word_len = len(words[0])
        words_len = len(words) * word_len

        chunk_letters_map = {}

        if len(s)< words_len:
            return []

        for i in range(0, words_len):
            self.inc_map(chunk_letters_map, s[i])

        ans = []

        p = 0

        while p < len(s) - words_len:
            if chunk_letters_map == words_letters_map:
                chunk_words_map = self.create_words_map(
                    self.split_string(s, p, words_len, word_len)
                )

                if chunk_words_map == words_map:
                    ans.append(p)

            self.dec_map(chunk_letters_map, s[p])

            self.inc_map(chunk_letters_map, s[p + words_len])
            
            p += 1

        if chunk_letters_map == words_letters_map:
            chunk_words_map = self.create_words_map(
                self.split_string(s, p, words_len, word_len)
            )

            if chunk_words_map == words_map:
                ans.append(p)

        return ans
    
    def inc_map(self, map: dict[str, int], letter: str):
        map[letter] = map[letter] + 1 if letter in map else 1

    def dec_map(self, map: dict[str, int], letter: str):
        map[letter] -= 1

        if map[letter] == 0:
            map.pop(letter)

    def split_string(self, s: str, offset: int, length: int, chunk_size: int) -> List[str]:
        return [s[i:i+chunk_size] for i in range(offset, offset + length, chunk_size)]
    
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
