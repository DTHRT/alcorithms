# Task: https://neetcode.io/problems/anagram-groups
# Solution
# Time: O(n)
# Memory: O(n)

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(word)

        return list(res.values())


solution = Solution()


def test_group_anagrams():
    assert solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]) == [["act","cat"],["pots","tops","stop"],["hat"]]


solution.groupAnagrams(["qwe", "ewq", "asd"])