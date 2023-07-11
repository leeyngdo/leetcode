class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp = [None for i in range(n)]
        self.dp[0] = 1 
        if n >= 2:
            self.dp[1] = 2

        return self.recursion(n)

    def recursion(self, n):
        if self.dp[n - 1] != None:
            return self.dp[n - 1]
        else:
            self.dp[n - 1] = self.recursion(n - 1) + self.recursion(n - 2)

            return self.dp[n - 1]