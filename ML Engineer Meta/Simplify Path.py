def simplifyPath(path: str) -> str :
    canon = []

    for string in path.split("/") :
        if string == '' or string == '.' :
            continue
        elif string == '..' :
            if len(canon) > 0 :
                canon.pop()
        else :
            canon.append(string)

    return "/" + "/".join(canon)

a = simplifyPath("/home/user/Documents/../Pictures")

print(a)