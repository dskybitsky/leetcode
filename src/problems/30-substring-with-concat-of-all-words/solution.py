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

        words_letters_dict = {}

        for word in words:
            for letter in word:
                self.inc_dict(words_letters_dict, letter)

        word_len = len(words[0])
        words_len = len(words) * word_len

        chunk_letters_dict = {}

        if len(s)< words_len:
            return []

        for i in range(0, words_len):
            self.inc_dict(chunk_letters_dict, s[i])

        ans = []

        p = 0

        while p < len(s) - words_len:
            if chunk_letters_dict == words_letters_dict:
                chunk_words_dict = self.create_words_dict(
                    self.split_string(s, p, words_len, word_len)
                )

                if chunk_words_dict == words_dict:
                    ans.append(p)

            self.dec_dict(chunk_letters_dict, s[p])

            self.inc_dict(chunk_letters_dict, s[p + words_len])
            
            p += 1

        if chunk_letters_dict == words_letters_dict:
            chunk_words_dict = self.create_words_dict(
                self.split_string(s, p, words_len, word_len)
            )

            if chunk_words_dict == words_dict:
                ans.append(p)

        return ans
    
    def inc_dict(self, dict: Dict[str, int], letter: str):
        dict[letter] = dict[letter] + 1 if letter in dict else 1

    def dec_dict(self, dict: Dict[str, int], letter: str):
        dict[letter] -= 1

        if dict[letter] == 0:
            dict.pop(letter)

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
