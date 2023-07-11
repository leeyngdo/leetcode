class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x % 10 == x:
            return True
        else:
            tmp = x; new = 0  
            while tmp > 0:
                new = new * 10 + tmp % 10
                tmp = tmp // 10
            return new == x