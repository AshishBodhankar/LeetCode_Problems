from collections import defaultdict
def canFinish(numCourses: int, prerequisites: list) -> bool:

    adj_l = defaultdict(list)

    for course, prereq in prerequisites:
        adj_l[course].append(prereq)

    UNVISITED = 0
    VISITING = 1
    VISITED = 2

    states = [UNVISITED]*numCourses

    def dfs(course):

        state = states[course]

        if state == VISITED:
            return True
        elif state == VISITING:
            return False

        states[course] = VISITING

        for nei in adj_l[course]:
            if not dfs(nei):
                return False
        states[course] = VISITED
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True