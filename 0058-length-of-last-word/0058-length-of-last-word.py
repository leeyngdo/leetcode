class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = len(s) - 1; left = right - 1; ans = 0
        
        while ans == 0 and left >= 0:
            if s[right].isalnum() and s[left].isalnum():
                pass
            else:
                if s[right].isalnum():
                    ans = right - left
                right = left
            
            left -= 1
        
        if s[right].isalnum():
            ans = right + 1
        return ans