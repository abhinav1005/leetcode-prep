# Problem: Valid Anagram (LC #242)
# Link: https://leetcode.com/problems/valid-anagram/
#
# Approach: Count character frequencies in both strings and compare.
#           Two strings are anagrams if they have the same char counts.
# Time: O(n) | Space: O(1) - at most 26 chars in counter
#
# Pattern: Arrays & Hashing

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    # Alternative: manual count with array (26 lowercase letters)
    def isAnagram_v2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1
        return all(x == 0 for x in count)


# Quick test
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
