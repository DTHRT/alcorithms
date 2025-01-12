# Task: https://neetcode.io/problems/products-of-array-discluding-self
# Solution
# Time: O(n)
# Memory: O(n)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        output = [1] * len(nums)

        # nums = [1,2,4,6]
        # Left-To-Right fill up prefix, index = 0 -> prefix[0] = nums[0]:
        i = 0
        while i < len(nums):  # [1,2,4,6]
            if i == 0:
                prefix[0] = nums[0]
                i += 1
                continue

            prefix[i] = prefix[i - 1] * nums[i]
            i += 1

        # prefix: [1, 2, 8, 48]

        # Right-To-Left fill up postfix, index = -1 -> postfix[-1] = nums[-1]:
        i = len(nums) - 1
        while i >= 0:  # [1,2,4,6]
            if i == len(nums) - 1:
                postfix[-1] = nums[-1]
                i -= 1
                continue

            postfix[i] = postfix[i+1] * nums[i]
            i -= 1

        # postfix: [48, 48, 24, 6]

        # Fill up output:
        i = 0
        while i < len(nums):
            if i == 0:
                output[i] = 1 * postfix[i+1]
                i += 1
                continue

            if i == len(nums) - 1:
                output[i] = prefix[i-1] * 1
                i += 1
                continue

            output[i] = prefix[i-1] * postfix[i+1]
            i += 1

        #           0 , 1 , 2 , 3
        # input    [1 , 2 , 4 , 6]
        # prefix:  [1 , 2 , 8 , 48]
        # postfix: [48, 48, 24, 6]
        # ouput:   [48, 24, 12, 8]

        return output


solution = Solution()


def test():
    assert solution.productExceptSelf([1, 2, 4, 6]) == [48, 24, 12, 8]