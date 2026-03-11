# Problem: Group Anagrams (LC #49)
# Link: https://leetcode.com/problems/group-anagrams/
#
# Approach: Use a hash map where each key is a 26-length tuple representing
#           character frequencies, and each value is the list of strings in
#           that anagram group. Avoids sorting (O(n log n)) by using a count array.
# Time: O(n * k) where k = avg string length | Space: O(n)
#
# Algorithm:
#   - For each string, build a count array of size 26 (one slot per letter).
#   - Convert the count array to a tuple (hashable) and use it as the dict key.
#   - Append the string to its anagram group.
#   - Return all the grouped lists.
#
# Pattern: Arrays & Hashing

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord('a')] += 1
            seen[tuple(count)].append(s)
        return list(seen.values())


# Quick test
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
