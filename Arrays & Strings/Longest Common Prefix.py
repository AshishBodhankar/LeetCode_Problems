## My solution
def longestCommonPrefix(strs: list) -> str:
    result = ""
    i = 0
    shortest = min([len(str) for str in strs])
    while i < shortest:
        if len(set(str[i] for str in strs)) == 1:
            result += strs[0][i]
            i += 1
        else:
            break
    return result

# Gregg's solution
def longestCommonPrefix2(strs: list) -> str:
    shortest = float('inf')

    for s in strs:
        if len(s) < shortest:
            shortest = len(s)

    i = 0
    while i < shortest:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i += 1

    return s[:i]

print(longestCommonPrefix2(["flower","flow","flight"]))


