# TIME: O(N^2)
def isSubsequence(s: str, t: str) -> bool:
    if all(ss in t for ss in s):
        return True
    else:
        return False


def isSubsequence2(s: str, t: str) -> bool:
    S = len(s)
    T = len(t)
    if s == '': return True
    if S > T: return False
    j = 0
    for i in range(T):
        if t[i] == s[j]:
            if j == S-1:
                return True
            j += 1

    return False
    # TIME: O(N

print(isSubsequence2('abc','ahbgdc'))


for i in range(T):
    if s[j] == t[i]:
        if j == S-1
        j += 1
