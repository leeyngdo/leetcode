class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2: return x

        # We want to find `sqrt` s.t. f(sqrt) = sqrt^2 - x = 0.
        # Newton-Raphson: sqrt = sqrt - (sqrt^2 - x) / (2 * sqrt)
        sqrt = x // 2
        while sqrt * sqrt > x:
            sqrt = (sqrt + x / sqrt) // 2
        return sqrt

        