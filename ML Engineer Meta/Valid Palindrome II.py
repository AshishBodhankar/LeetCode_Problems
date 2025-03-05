def validPalindrome(self, s: str) -> bool :

    S = len(s)

    def ispalindrome(s: str) -> bool :
        # len(s) is odd
        if len(s) & 1 == 1 :
            mid = len(s) // 2
            return s[mid - 1 : :-1] == s[mid + 1 :]
        else :
            mid_h = S // 2
            mid_l = mid_h - 1
            return s[mid_l : :-1] == s[mid_h :]

    if ispalindrome(s) or len(s) <= 2 :
        return True

    l, r = 0, S - 1
    while s[l] == s[r] and l < r :
        l += 1
        r -= 1

    return ispalindrome(s[:l] + s[l + 1 :]) or ispalindrome(s[:r] + s[r + 1 :])


