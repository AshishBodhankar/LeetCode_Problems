
def trap(height: list):
    """
    CONSTRAINTS
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105

    :param height: List[int]
    :return: int
    """
    n = len(height)
    l_max, r_max = [0]*n, [0]*n
    l = r = summ = 0

    for i in range(n):
        j = - i - 1

        l_max[i], r_max[j] = l, r

        l, r = max(l, height[i]), max(r, height[j])

    for k in range(n):
        depth = min(l_max[k], r_max[k])
        summ += max(depth-height[k], 0)

    return summ





