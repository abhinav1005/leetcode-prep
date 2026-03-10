# ============================================================
# Python Sorting & Binary Search - Foundations
# ============================================================

# ---- SORTING ----

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# In-place sort
nums.sort()                         # ascending
nums.sort(reverse=True)             # descending

# Returns new sorted list
sorted_nums = sorted(nums)
sorted_nums = sorted(nums, reverse=True)

# Sort by key
words = ["banana", "apple", "cherry"]
words.sort(key=len)                         # by length
words.sort(key=lambda x: x[-1])            # by last char

pairs = [(1, 3), (2, 1), (3, 2)]
pairs.sort(key=lambda x: x[1])             # by second element
pairs.sort(key=lambda x: (x[1], x[0]))     # multi-key sort


# ---- BINARY SEARCH ----

def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


# Find leftmost position to insert target
def bisect_left_manual(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


# bisect module (standard library)
import bisect
nums = [1, 3, 5, 7, 9]
bisect.bisect_left(nums, 5)     # 2 - leftmost insert pos
bisect.bisect_right(nums, 5)    # 3 - rightmost insert pos
bisect.insort(nums, 6)          # insert in sorted order


# ---- COMMON BINARY SEARCH TEMPLATES ----

# Find min k where condition(k) is True
def binary_search_min(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if condition(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

# Find max k where condition(k) is True
def binary_search_max(lo, hi):
    while lo < hi:
        mid = (lo + hi + 1) // 2   # upper mid to avoid infinite loop
        if condition(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo

def condition(k):
    pass  # define your condition
