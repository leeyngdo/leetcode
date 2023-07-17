# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return n
        
        lo = 1; hi = n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if guess(mid) > 0:
                lo = mid + 1
            else:
                hi = mid
        
        return lo