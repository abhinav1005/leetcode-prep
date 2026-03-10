# Problem: Two Sum (LC #1)
# Link: https://leetcode.com/problems/two-sum/
#
# Approach: Use a hash map to store {value: index} as we iterate.
#           For each number, check if (target - value) is already in the map.
#           If so, we found our pair.
# Time: O(n) | Space: O(n)
#
# Pattern: Arrays & Hashing

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            if (target - value) in seen:
                return [seen.get(target - value), index]
            else:
                seen[value] = index


# Quick test
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))         # [1, 2]
