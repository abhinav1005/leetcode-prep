# Problem: Contains Duplicate (LC #217)
# Link: https://leetcode.com/problems/contains-duplicate/
#
# Approach: Use a hash set. For each number, if it's already in the set
#           we found a duplicate. Otherwise add it.
# Time: O(n) | Space: O(n)
#
# Pattern: Arrays & Hashing

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


# Quick test
if __name__ == "__main__":
    s = Solution()
    print(s.hasDuplicate([1, 2, 3, 1]))  # True
    print(s.hasDuplicate([1, 2, 3, 4]))  # False
