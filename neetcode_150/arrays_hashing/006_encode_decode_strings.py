# Problem: Encode and Decode Strings (LC #271)
# Link: https://leetcode.com/problems/encode-and-decode-strings/
#
# Approach: Encode each string as "length#string". The length prefix tells
#           the decoder exactly how many characters to read, so '#' inside
#           a string never causes ambiguity.
# Time: O(n) encode, O(n) decode | Space: O(n)
#
# Algorithm:
#   Encode:
#     - For each string, append "len(s)#s" to the result.
#   Decode:
#     - Use pointer i. Find '#' with pointer j, parse the length.
#     - Move i past '#', extract the next `length` chars as the original string.
#     - Advance i and repeat until end.
#
# Pattern: Arrays & Hashing

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        toRet = ""

        for s in strs:
            toRet += str(len(s)) + "#" + s
        return toRet

    def decode(self, s: str) -> List[str]:
        toRet = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            i = j + 1
            j = i + count
            toRet.append(s[i:j])
            i = j
        return toRet


# Quick test
if __name__ == "__main__":
    sol = Solution()
    words = ["neet", "code", "loves", "you"]
    encoded = sol.encode(words)
    print(encoded)              # "4#neet4#code5#loves3#you"
    print(sol.decode(encoded))  # ['neet', 'code', 'loves', 'you']
