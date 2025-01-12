# Task: https://neetcode.io/problems/string-encode-and-decode
# Solution
# Time: O(m)
# Memory: O(1)
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


solution = Solution()


def test_encode():
    assert solution.encode(["neet","code","love","you"]) == "4#neet4#code4#love3#you"


def test_decode():
    assert solution.decode("4#neet4#code4#love3#you") == ["neet","code","love","you"]