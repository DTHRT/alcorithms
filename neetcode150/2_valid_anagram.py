# Mine:
# Task: https://neetcode.io/problems/is-anagram
# Time: O(nlogn + mlogm)
# Memory: O(n + m) or 0(1) depends on sorting algo

# class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        if sorted(list(s)) == sorted(list(t)):
#            return True
#        return False


# Solution 1:
# Time: O(n)
# Memory: O(n)


# class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        if len(s) != len(t):
#            return False
#
#        countS, countT = {}, {}
#
#        for i in range(len(s)):
#            countS[s[i]] = 1 + countS.get(s[i], 0)
#            countT[t[i]] = 1 + countT.get(t[i], 0)
#
#        for c in countS:
#            if countS[c] != countT.get(c, 0):
#                return False
#
#        return True


# Solution 2 [BEST]:
# Time: 0(n + m)
# Memory: 0(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False

        return True


solution = Solution()


def test_is_anagram():
    assert solution.isAnagram("anagram", "nagaram") == True

def test_is_not_anagram():
    assert solution.isAnagram("rat", "car") == False