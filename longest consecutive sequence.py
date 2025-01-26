# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must  write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = `[100, 4, 200, 1, 3, 2]`
# Output: 4

# Example 2:
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9

from typing import List

## the below code does not in O(n) time. It is unoptimized and basic
def longestConsecutive(nums: List[int]) -> int:
    items = list(set(nums))
    items.sort()

    count = 1
    length = 1
    for i in range(1, len(items)):
        if items[i] == items[i - 1] + 1:
            count = count + 1
            length = max(length, count)
        else:
            count = 1
    return length

## more Optimized code that runs in O(n) time
def longestConsecutive2(nums: List[int]) -> int:
    s = set(nums)
    longest = 0
    for num in s:
        if num-1 not in s:
            curr = 1
            while num+1 in s:
                curr += 1
                num += 1
            longest = max(longest, curr)
    return longest
