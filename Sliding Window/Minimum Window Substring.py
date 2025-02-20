from collections import Counter
def minWindow(s: str, t: str) -> str:
    """
    Leetcode # 76: Minimum Window Substring
    :param s: string containing uppercase and lowercase alphabets
    :param t: string containing uppercase and lowercase alphabets
    :return: minimum window substring of s that contains t
    """
    S = len(s)
    T = len(t)

    dict_t = Counter(t)
    target = len(dict_t)

    dict_window = {}
    formed = 0

    ans = float("inf"),0,0

    # create two pointers for sliding window
    l,r = 0,0

    while r < S:
        char = s[r]

        dict_window[char] = dict_window.get(char,0) + 1

        if char in dict_t and dict_window[char] == dict_t[char]:
            formed += 1

        while formed == target and l <= r:

            if r-l+1 < ans[0]:
                ans = r - l + 1, l, r

            char = s[l]

            dict_window[char] -= 1

            if char in dict_t and dict_window[char] < dict_t[char]:
                formed -= 1

            l += 1

        r += 1

    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]

