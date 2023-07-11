# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1; e = n
        
        def check(self, idx):
            return 

        while s <= e:
            pivot = s + (e - s) // 2
            if isBadVersion(pivot):
                if not isBadVersion(pivot - 1):
                    return pivot
                else:
                    e = pivot - 1
            else:
                if isBadVersion(pivot + 1):
                    return pivot + 1
                else:
                    s = pivot + 1

        if s == e and isBadVersion(s):
            return s
        else:
            return -1