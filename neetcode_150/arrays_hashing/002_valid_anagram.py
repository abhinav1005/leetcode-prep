# Problem: Valid Anagram (LC #242)
# Link: https://leetcode.com/problems/valid-anagram/
#
# Approach: Build frequency maps for both strings using dicts, compare them.
#           Early exit if lengths differ.
# Time: O(n) | Space: O(n)
#
# Pattern: Arrays & Hashing

from collections import Counter

class Solution:
    # Approach 1: Manual frequency maps
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = {}
        t_list = {}
        for i in range(len(s)):
            s_list[s[i]] = 1 + s_list.get(s[i], 0)
            t_list[t[i]] = 1 + t_list.get(t[i], 0)
        return s_list == t_list

    # Approach 2: Counter (cleaner, same complexity)
    def isAnagram_v2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Quick test
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
