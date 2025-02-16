def subsets(nums: list):
    n = len(nums)

    res,sol = [],[]

    def backtrack(i):

        if i == n:
            res.append(sol[:])
            #print(sol[:])
            return

        # Don't pick nums[i]
        backtrack(i+1)

        # Pick nums[i]
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()

    backtrack(0)
    return res