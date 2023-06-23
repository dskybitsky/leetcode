from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_a = ord('a')

        order_idx = [0]* 26

        for i in range(26):
            c = order[i]
            order_idx[ord(c) - ord_a] = i


        def translate(word: str) -> str:
            res = ""

            for c in word:
                res += chr(order_idx[ord(c) - ord_a] + ord_a)

            return res
        
        words_tr = list(map(lambda w: translate(w), words))

        return words_tr == sorted(words_tr)


sol = Solution()

assert sol.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz") is True
assert sol.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz") is False
assert sol.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz") is False
