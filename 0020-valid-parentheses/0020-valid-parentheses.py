class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_len = len(s)
        
        seen = dict()
        LEFT = ['(', '[', '{']
        RIGHT = [')', ']', '}']
        PAIR = {'(': ')', '[': ']', '{': '}'}

        stack = []
        for par in s:
            if par in LEFT:
                stack.append(par)
            elif len(stack) == 0 or PAIR[stack.pop()] != par:
                return False

        return len(stack) == 0