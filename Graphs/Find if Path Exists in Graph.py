from collections import defaultdict
def validPath(n: int, edges: list, source: int, destination: int) -> bool:
    """
    LeetCode problem # 1971
    :param n: total no. of nodes in the graph
    :param edges: 2 array representing edges.
    :param source: int
    :param destination: int
    :return: bool
    """
    if source == destination:
        return True

    adj_l = defaultdict(list)

    for u,v in edges:
        adj_l[u].append(v)
        adj_l[v].append(u)

    seen = set()
    seen.add(source)
    stack = [source]

    while stack:
        node = stack.pop()
        if node == destination:
            return True
        for nei in adj_l[node]:
            if nei not in seen:
                seen.add(nei)
                stack.append(nei)
    return False