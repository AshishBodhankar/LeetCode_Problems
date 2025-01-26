## O(n) time and O(1) space
def majorityElement(nums: list) -> int:
    majority = None
    count = 0

    for num in nums:
        if count == 0:
            majority = num

        count += 1 if num == majority else -1
