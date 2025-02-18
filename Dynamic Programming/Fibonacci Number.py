class Solution :
    def fib(self, n: int) -> int :

        """
        Let's Solve this using recursion. Observe that this solution has a high runtime
        Time: O(2**n)
        Space: O(n)
        """
        if n == 0 :
            return 0
        elif n == 1 :
            return 1
        else :
            return self.fib(n - 1) + self.fib(n - 2)


class Solution :
    cache = defaultdict(int)
    cache[0] = 0
    cache[1] = 1

    def fib(self, n: int) -> int :

        """
        Let's Solve this using Top Down DP - Memoization
        Time: O(n)
        Space: O(n)
        """

        if n in self.cache :
            return self.cache[n]

        else :
            self.cache[n] = self.cache[n - 1] + self.cache[n - 2]
            return self.cache[n]


class Solution :
    def fib(self, n: int) -> int :

        """
        Solve this using Bottoms Up - Tabulation method
        Time:
        Space:
        """
        if n == 0 :
            return 0
        elif n == 1 :
            return 1

        else :
            prev = 0
            curr = 1
            for i in range(2, n + 1) :
                curr, prev = curr + prev, curr

        return curr
