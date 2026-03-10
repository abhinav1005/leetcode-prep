# Problem: Contains Duplicate (LC #217)
# Link: https://leetcode.com/problems/contains-duplicate/
#
# Approach: Use a hash set. For each number, if it's already in the set
#           we found a duplicate. Otherwise add it.
# Time: O(n) | Space: O(n)
#
# Pattern: Arrays & Hashing

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


# Quick test
if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))  # True
    print(s.containsDuplicate([1, 2, 3, 4]))  # False
