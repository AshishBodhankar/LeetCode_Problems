def permute(nums: list):
    n = len(nums)
    res, sol = [],[]

    def backtrack():
        if len(sol) == n:
            res.append(sol[:])
            return

        for num in nums:
            if num not in sol:
                sol.append(num)
                backtrack()
                #print(sol[:])
                sol.pop()

    backtrack()
    return res