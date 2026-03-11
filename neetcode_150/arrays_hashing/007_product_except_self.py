# Problem: Product of Array Except Self (LC #238)
# Link: https://leetcode.com/problems/product-of-array-except-self/
#
# Approach: Two passes over the array — no division, O(1) extra space.
#           First pass (left to right): res[i] = product of all elements to the left.
#           Second pass (right to left): multiply res[i] by product of all elements to the right.
# Time: O(n) | Space: O(1) extra (output array doesn't count)
#
# Algorithm:
#   - Init res = [1] * n and prefix = 1.
#   - Left pass: res[i] = prefix, then prefix *= nums[i].
#   - Right pass: res[i] *= postfix, then postfix *= nums[i] (iterating right to left).
#   - Return res.
#
# Pattern: Arrays & Hashing

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        toret = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            toret[i] *= prefix
            prefix *= nums[i]

        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            toret[i] *= prefix
            prefix *= nums[i]

        return toret


# Quick test
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(sol.productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
