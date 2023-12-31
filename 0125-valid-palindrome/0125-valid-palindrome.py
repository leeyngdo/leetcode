class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            elif not s[end].isalnum():
                end -= 1
                continue
            elif s[start].lower() != s[end].lower():
                return False
            
            start += 1; end -= 1
            
        return True
