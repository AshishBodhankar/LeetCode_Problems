# SOlUTION 1
def numJewelsInStones(jewels: str, stones: str) -> int:
    """

    :param jewels: representing the types of stones that are jewels,
    :param stones: representing the stones you have
    :return: You want to know how many of the stones you have are also jewels.
    """

    jewels = set(jewels)

    ans = 0

    for stone in stones:
        if stone in jewels:
           ans += 1
    return ans

# SOLUTION 2:
def numJewelsInStones2(jewels: str, stones: str) -> int :
    """

    :param jewels: representing the types of stones that are jewels,
    :param stones: representing the stones you have
    :return: You want to know how many of the stones you have are also jewels.
    """
    dict = {}

    for jewel in jewels :
        if jewel not in dict :
            dict[jewel] = 1
        else :
            dict[jewel] += 1
    for stone in stones :
        if stone in dict :
            dict[stone] += 1


    final_count = 0
    for jewel, count in dict.items() :
        count -= 1
        final_count += count

    return final_count
