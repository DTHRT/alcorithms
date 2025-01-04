from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


solution = Solution()


def test_top_k_frequent():
    assert solution.topKFrequent([1,2,2,3,3,3], 2) == [2,3] or [3,2]
    assert solution.topKFrequent([7,7], 1) == [7]