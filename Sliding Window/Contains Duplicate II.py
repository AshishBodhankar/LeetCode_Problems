def containsNearbyDuplicate(nums: list, k: int) -> bool:
    """
    Leetcode question no. 219
    :param nums: list of integers
    :param k: Maximum width allowed between two unique indices i and j
    :return: True if nums[i] == nums[j] such that abs(i-j) <= k
    """
    seen = set()

    for index,num in enumerate(nums):

        if index > k:
            seen.remove(nums[index-k-1])

        if num in seen:
            return True

        seen.add(num)

    return False