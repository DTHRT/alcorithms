from typing import List

# Task: https://neetcode.io/problems/duplicate-integer
# Solution
# Time: O(n)
# Memory: O(n)


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False


solution = Solution()


def test_no_duplicates():
    assert solution.hasDuplicate([1, 2, 3, 4]) == False


def test_with_duplicates():
    assert solution.hasDuplicate([1, 2, 3, 2, 5]) == True


def test_empty_list():
    assert solution.hasDuplicate([]) == False


def test_all_the_same():
    assert solution.hasDuplicate([7, 7, 7, 7]) == True
