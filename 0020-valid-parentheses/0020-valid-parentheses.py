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
            else:
                if len(stack) == 0:
                    return False
                
                left = stack.pop()
                pair = PAIR[left]

                if pair == par:
                    continue
                else:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True