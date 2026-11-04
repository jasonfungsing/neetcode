class Solution:

    def climbStairs(self, n: int) -> int:
        d ={}

        def helper(i):
            if i <= 1:
                return 1
            if i in d:
                return d[i]

            d[i] = helper(i - 1) + helper(i - 2)
            return d[i]
        
        return helper(n)