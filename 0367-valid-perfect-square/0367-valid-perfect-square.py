class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num